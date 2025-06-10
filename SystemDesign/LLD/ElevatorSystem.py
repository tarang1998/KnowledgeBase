# Requirements / Understanding 
# Multiple Elevators within a building with multiple floors 
# Users can request elevators from different floors, and can make request within the elevator 
# Optimize Elevator assignment to minimize the wait time
# Handle edge cases like power outage and maintainance  

from abc import ABC, abstractmethod
from typing import Optional

# ENUMS 
class DIRECTION:
    UP = "UP"
    DOWN = "DOWN" 
    IDLE = "IDLE"

class ELEVATOR_STATE:
    IDLE= "IDLE"
    RUNNING = "RUNNING"

# Observer Pattern 
class ElevatorObserver(ABC):
    @abstractmethod
    def on_state_change(self,elevator,state):
        pass
    @abstractmethod
    def on_floor_change(self,elevator,floor):
        pass
    
class ElevatorDisplay(ElevatorObserver):
    def __init__(self,id):
        self.id = id
    def on_state_change(self,state):
        print("State Changed", id,state)
    def on_floor_change(self,floor):
        print("Floor Changed", id,floor)
 

# Command Pattern 
class ElevatorCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

class InternalElevatorRequest(ElevatorCommand):
    def __init__(self,floor):
        self.floor = floor 

    def execute(self):
        pass


class ExternalElevatorRequest(ElevatorCommand):
    def __init__(self,floor,direction):
        self.floor = floor 
        self.direction = direction
    def execute(self):
        pass


# Scheduling Stratergy
class SchedulingStrategy(ABC):
    @abstractmethod
    def get_next_stop(self):
        pass

class LookSchedulingStatergy(SchedulingStrategy):
    def get_next_stop(self,elevator):
        currentFloor = elevator.currentFloor
        if not elevator.requests:
            return currentFloor
        targetFloor = elevator.requests[0].floor 
        direction = None 
        if targetFloor>currentFloor:
            direction = DIRECTION.UP 
        elif targetFloor<currentFloor:
            direction = DIRECTION.DOWN
        else: 
            return currentFloor

        bestPick = None
        for req in elevator.requests:
            f = req.floor 
            if direction == DIRECTION.UP and f > currentFloor and f <= targetFloor:
                if (isinstance(req,InternalElevatorRequest) or (isinstance(req,ExternalElevatorRequest) and req.direction == DIRECTION.UP)):
                    print("R")
                    if bestPick == None or f < bestPick:
                        bestPick = f
            if direction == DIRECTION.DOWN and f < currentFloor and f >= targetFloor:
                if (isinstance(req,InternalElevatorRequest) or (isinstance(req,ExternalElevatorRequest) and req.direction == DIRECTION.DOWN)):
                    if bestPick == None or f > bestPick:
                        bestPick = f 
        print(currentFloor,targetFloor,bestPick,direction)
        return bestPick if bestPick != None else targetFloor
        

# Elevator 
class Elevator:
    def __init__(self,id,currentFloor,direction,state,observers,requests):
        self.id = id
        self.currentFloor = currentFloor
        self.direction = direction
        self.state = ELEVATOR_STATE.IDLE
        self.observers = observers
        self.requests = requests


    def accept_request(self,request):
        self.requests.add(request)
        
    def add_observer(self, obs: ElevatorObserver) -> None:
        self.observers.append(obs)

    def _notify_state(self) -> None:
        for o in self.observers:
            o.on_state_change(self.state)

    def _notify_floor(self) -> None:
        for o in self.observers:
            o.on_floor_change(self.currentFloor)

    def move_to_next_stop(self,next_stop):
        self.state= ELEVATOR_STATE.RUNNING
        self._notify_state()
        while (self.currentFloor != next_stop):
            if next_stop > self.currentFloor:
                self.direction = DIRECTION.UP
                self.currentFloor += 1
                self._notify_floor() 
            if next_stop < self.currentFloor:
                self.direction = DIRECTION.DOWN
                self.currentFloor -= 1 
                self._notify_floor() 
        self.arrived_at_stop()

    def arrived_at_stop(self):
        self.state = ELEVATOR_STATE.IDLE
        self._notify_state()
        filteredRequests = []
        if not self.requests:
            self.direction = DIRECTION.IDLE
            return 
        for req in self.requests:
            if isinstance(req,InternalElevatorRequest):
                if req.floor == self.currentFloor:
                    continue
            elif isinstance(req,ExternalElevatorRequest):
                if req.floor == self.currentFloor and req.direction == self.direction:
                    continue    
            filteredRequests.append(req)
        print("Requests Pending", self.id, filteredRequests)
        self.requests = filteredRequests



class ElevatorController:
    def __init__(self,elevators,floors,schedulingStratergy):
        self.elevators = [Elevator(i+1,0,DIRECTION.IDLE,ELEVATOR_STATE.IDLE,[ElevatorDisplay(i+1)],[]) for i in range(elevators)]
        self.floors = floors
        self.schedulingStratergy = schedulingStratergy

    def request_elevator(self, elevatorId, currentFloorNo, direction):
        print("Adding request for elevator :",elevatorId,currentFloorNo,direction)
        elevator = self._find(elevatorId)
        if not elevator:
            print("Elevator not found")
        elevator.requests.append(ExternalElevatorRequest(currentFloorNo,DIRECTION.UP if direction == 1 else DIRECTION.DOWN))

    def request_floor(self,elevatorId,floorNo):
        print("Adding request in elevator :",elevatorId,floorNo)
        elevator = self._find(elevatorId)
        if not elevator:
            print("Elevator not found")
        elevator.requests.append(InternalElevatorRequest(floorNo))

    def step(self):
        for ele in self.elevators:
            if ele.requests:
                nextStop = self.schedulingStratergy.get_next_stop(ele)
                if nextStop != ele.currentFloor:
                    ele.move_to_next_stop(nextStop)

    def displayElevatorStatuses(self):
        for ele in self.elevators:
            print(ele.id,ele.state,ele.currentFloor)

    def _find(self, eid: int) -> Optional[Elevator]:
        for e in self.elevators:
            if e.id == eid:
                return e
        return None


class Building:
    def __init__(self, name: str, floors: int, controller):
        self.name = name
        self.floors = floors
        self.elevatorController = controller


if __name__ == "__main__":

    scheduling = LookSchedulingStatergy()
    elevatorController = ElevatorController(4,20,scheduling)
    building = Building("Tarang", 20 ,elevatorController)

    isRunning = True 
    while isRunning:
        print("1. Make an external request ")
        print("2. Make internal request")
        print("3. Similuate next step")
        print("4. Exit")

        choice = int(input("Enter choice : "))
        if choice == 1:
            id = int(input("Enter Elevator Id : "))
            floor = int(input("Enter current floor : "))
            direction = int(input("Enter elevator direction : 1 for up 0 for down : "))
            elevatorController.request_elevator(id,floor,direction)
            continue
        if choice == 2:
            id = int(input("Enter Elevator Id : "))
            floor = int(input("Enter destination floor : "))
            elevatorController.request_floor(id,floor)
            continue
        if choice == 3:
            elevatorController.step()
            elevatorController.displayElevatorStatuses()
            continue
        else:
            break




    