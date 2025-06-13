from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from threading import Lock
from enum import Enum, auto
from collections import deque

# ----------------------------
# Enums
# ----------------------------
class VehicleType(Enum):
    CAR = auto()
    BIKE = auto()
    TRUCK = auto()

class PaymentMethod(Enum):
    CASH = auto()
    CARD = auto()
    UPI = auto()

# ----------------------------
# Strategy: Parking Fee
# ----------------------------
class ParkingFeeStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, vehicle_type: VehicleType, duration: timedelta) -> float:
        pass

class BasicHourlyRate(ParkingFeeStrategy):
    RATES = {
        VehicleType.CAR: 10.0,
        VehicleType.BIKE: 5.0,
        VehicleType.TRUCK: 15.0
    }

    def calculate_fee(self, vehicle_type: VehicleType, duration: timedelta) -> float:
        hours = max(1, int(duration.total_seconds() // 3600))
        rate = self.RATES.get(vehicle_type, 20.0)
        return hours * rate

class PremiumRate(ParkingFeeStrategy):
    MULTIPLIER = 1.5

    def __init__(self):
        self.basic = BasicHourlyRate()

    def calculate_fee(self, vehicle_type: VehicleType, duration: timedelta) -> float:
        return self.basic.calculate_fee(vehicle_type, duration) * self.MULTIPLIER

# ----------------------------
# Strategy: Payment
# ----------------------------
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class CashPayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"[Cash] Collected ${amount:.2f}")
        return True

class CardPayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"[Card] Charged ${amount:.2f}")
        return True

class UPIPayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"[UPI] Transferred ${amount:.2f}")
        return True

# ----------------------------
# Factory: Vehicles
# ----------------------------
class Vehicle(ABC):
    def __init__(self, license_plate: str, fee_strategy: ParkingFeeStrategy):
        self.license_plate = license_plate
        self.fee_strategy = fee_strategy
        self.entry_time: datetime = None

    @property
    @abstractmethod
    def type(self) -> VehicleType:
        pass

    def enter(self):
        self.entry_time = datetime.now()

    def exit_duration(self) -> timedelta:
        return datetime.now() - self.entry_time

class Car(Vehicle):
    @property
    def type(self) -> VehicleType:
        return VehicleType.CAR

class Bike(Vehicle):
    @property
    def type(self) -> VehicleType:
        return VehicleType.BIKE

class Truck(Vehicle):
    @property
    def type(self) -> VehicleType:
        return VehicleType.TRUCK

class VehicleFactory:
    @staticmethod
    def create_vehicle(vtype: VehicleType, plate: str, fee_strategy: ParkingFeeStrategy) -> Vehicle:
        mapping = {
            VehicleType.CAR: Car,
            VehicleType.BIKE: Bike,
            VehicleType.TRUCK: Truck
        }
        cls = mapping.get(vtype, Car)
        v = cls(plate, fee_strategy)
        return v

# ----------------------------
# Parking Spots & Floors
# ----------------------------
class ParkingSpot:
    def __init__(self, spot_id: int, floor_no : int, spot_type: VehicleType):
        self.spot_id = spot_id
        self.floor_no = floor_no
        self.spot_type = spot_type
        self.vehicle: Vehicle = None

    def is_free(self) -> bool:
        return self.vehicle is None

    def park(self, vehicle: Vehicle):
        if not self.is_free():
            raise Exception("Spot already occupied")
        if vehicle.type != self.spot_type:
            raise Exception("Wrong spot type")
        vehicle.enter()
        self.vehicle = vehicle

    def vacate(self) -> Vehicle:
        if self.is_free():
            raise Exception("Spot already empty")
        v = self.vehicle
        self.vehicle = None
        return v

class ParkingFloor:
    def __init__(self, floor_no: int):
        self.floor_no = floor_no
        self.free_spots : dict[VehicleType, deque[ParkingSpot]] = {
            vt : deque() for vt in VehicleType
        }
        self.spots: list[ParkingSpot] = []

    def add_spots(self, spot_type: VehicleType, count: int):
        start = len(self.spots) + 1
        for i in range(count):
            spot = ParkingSpot(start + i, self.floor_no, spot_type)
            self.spots.append(spot)
            self.free_spots[spot_type].append(spot)

    def find_free_spot(self, vtype: VehicleType) -> ParkingSpot | None:
        dq = self.free_spots[vtype]
        return dq.popleft() if dq else None

# ----------------------------
# Singleton: Parking Lot
# ----------------------------
class ParkingLot:
    _instance = None
    _lock = Lock()

    def __init__(self):
        self.floors: list[ParkingFloor] = []
        self.observers = []

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
        return cls._instance

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def find_spot(self, vtype: VehicleType) -> ParkingSpot | None:
        for f in self.floors:
            spot = f.find_free_spot(vtype)
            if spot:
                return spot
        return None

    def _get_parking_floor(self,floor_no: int ) -> ParkingFloor:
        for floor in self.floors:
            if floor.floor_no == floor_no:
                return floor
        return None

    def park_vehicle(self, vehicle: Vehicle) -> ParkingSpot:
        spot = self.find_spot(vehicle.type)
        if not spot:
            raise Exception("No spot available")
        spot.park(vehicle)
        return spot

    def exit_vehicle(self, spot: ParkingSpot, payment: PaymentStrategy):
        vehicle = spot.vacate()
        floor_no = spot.floor_no
        parkingfloor = self._get_parking_floor(floor_no=floor_no)
        parkingfloor.free_spots[vehicle.type].append(spot)
        duration = datetime.now() - vehicle.entry_time
        fee = vehicle.fee_strategy.calculate_fee(vehicle.type, duration)
        if payment.pay(fee):
            self._notify_exit(vehicle, fee, duration)

    def register_observer(self, fn):
        self.observers.append(fn)

    def _notify_exit(self, vehicle, fee, duration):
        for fn in self.observers:
            fn(vehicle, fee, duration)

# ----------------------------
# Builder: Multi-Floor Setup
# ----------------------------
class ParkingLotBuilder:
    def __init__(self):
        self.parking_lot = ParkingLot()

    def create_floor(self, floor_no: int, car_spots: int, bike_spots: int, truck_spots: int):
        floor = ParkingFloor(floor_no)
        floor.add_spots(VehicleType.CAR, car_spots)
        floor.add_spots(VehicleType.BIKE, bike_spots)
        floor.add_spots(VehicleType.TRUCK, truck_spots)
        self.parking_lot.add_floor(floor)
        return self

    def build(self) -> ParkingLot:
        return self.parking_lot

# ----------------------------
# Demo
# ----------------------------
if __name__ == "__main__":
    # Build a 2-floor lot
    lot = (ParkingLotBuilder()
           .create_floor(1, car_spots=2, bike_spots=2, truck_spots=1)
           .create_floor(2, car_spots=1, bike_spots=1, truck_spots=1)
           .build())

    # Register an exit observer
    def on_exit(v, fee, dur):
        print(f"[Observer] {v.type.name} {v.license_plate} exited after {int(dur.total_seconds()//60)}m, paid ${fee:.2f}")

    lot.register_observer(on_exit)

    # Simulate
    fee_strat = BasicHourlyRate()
    v1 = VehicleFactory.create_vehicle(VehicleType.CAR, "CAR-123", fee_strat)
    spot1 = lot.park_vehicle(v1)
    print(f"Parked {v1.type.name} at spot {spot1.spot_id}")

    import time; time.sleep(2)  # simulate delay
    lot.exit_vehicle(spot1, CardPayment())
