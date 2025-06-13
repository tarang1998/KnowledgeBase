import threading
import uuid
from datetime import datetime, timedelta
from enum import Enum, auto 
from typing import List,Dict, Optional
from abc import ABC, abstractmethod


class BookingStatus(Enum):
    CREATED = auto()
    CONFIRMED = auto()
    EXPIRED = auto()


class SeatCategory(Enum):
    SILVER = auto()
    GOLD = auto()
    PLATINUM = ()



class Movie:
    def __init__(self, name: str, duration_minutes: int):
        self.id = uuid.uuid4().hex
        self.name = name
        self.duration_minutes = duration_minutes


class Seat:
    def __init__(self, row: int, category: SeatCategory):
        self.id = uuid.uuid4().hex
        self.row = row
        self.category = category


class Screen:
    def __init__(self, name: str):
        self.id = uuid.uuid4().hex
        self.name = name
        self.seats: List[Seat] = []

    def add_seat(self, seat: Seat):
        self.seats.append(seat)


class Show:
    def __init__(self, movie: Movie, screen: Screen, start_time: datetime):
        self.id = uuid.uuid4().hex
        self.movie = movie
        self.screen = screen
        self.start_time = start_time


class User:
    def __init__(self, name: str, email: str):
        self.id = uuid.uuid4().hex
        self.name = name
        self.email = email


class Booking:
    def __init__(self, user: User, show: Show, seats: List[Seat]):
        self.id = uuid.uuid4().hex
        self.user = user
        self.show = show
        self.seats = seats
        self.status = BookingStatus.CREATED

    def confirm(self):
        if self.status is not BookingStatus.CREATED:
            raise Exception("Cannot confirm booking not in CREATED state.")
        self.status = BookingStatus.CONFIRMED

    def expire(self):
        if self.status is not BookingStatus.CREATED:
            raise Exception("Cannot expire booking not in CREATED state.")
        self.status = BookingStatus.EXPIRED



class SeatLockStategy:
    def lock_seats(self, show: Show, seats: List[Seat], user: User):
        pass
    def unlock_seats(self, show: Show, seats: List[Seat], user: User):
        pass
    def validate_lock(self, show: Show, seat: Seat, user: User) -> bool:
        pass
    def get_locked_seats(self, show: Show) -> List[Seat]:
        pass



class InMemoryScreenLockProvider(SeatLockStategy):

    def __init__(self, timeout_seconds: int = 600):
        self.timeout = timedelta(seconds=timeout_seconds)
        self.locks: Dict[str, Dict[str, Dict]] = {}
        self._lock = threading.Lock()

    def lock_seats(self, show: Show, seats: List[Seat], user: User):
        now = datetime.now()
        with self._lock:
            show_locks = self.locks.setdefault(show.id, {})
            # Check existing locks
            for seat in seats:
                entry = show_locks.get(seat.id)
                if entry and now < entry['expires_at']:
                    raise Exception(f"Seat {seat.id} is already locked.")
            # Acquire locks
            for seat in seats:
                show_locks[seat.id] = {
                    'user_id': user.id,
                    'expires_at': now + self.timeout
                }

    def unlock_seats(self, show: Show, seats: List[Seat], user: User):
        with self._lock:
            show_locks = self.locks.get(show.id, {})
            for seat in seats:
                entry = show_locks.get(seat.id)
                if entry and entry['user_id'] == user.id:
                    del show_locks[seat.id]

    def validate_lock(self, show: Show, seat: Seat, user: User) -> bool:
        now = datetime.now()
        with self._lock:
            entry = self.locks.get(show.id, {}).get(seat.id)
            return bool(entry and entry['user_id'] == user.id and now < entry['expires_at'])

    def get_locked_seats(self, show: Show) -> List[Seat]:
        now = datetime.now()
        with self._lock:
            show_locks = self.locks.get(show.id, {})
            # Prune expired
            expired = [sid for sid, e in show_locks.items() if now >= e['expires_at']]
            for sid in expired:
                del show_locks[sid]
            return [seat_id for seat_id in show_locks.keys()]
        


class InMemorySeatLockProvider:
    def __init__(self, timeout_seconds: int = 600):
        self.timeout = timedelta(seconds=timeout_seconds)
        # For each show, map seat.id to lock metadata
        self.locks: Dict[str, Dict[str, Dict]] = {}
        # A lock per seat to synchronize at seat level
        self._seat_mutexes: Dict[str, threading.Lock] = {}

    def _get_mutex(self, seat_id: str) -> threading.Lock:
        # Create a mutex for each seat on demand
        if seat_id not in self._seat_mutexes:
            self._seat_mutexes[seat_id] = threading.Lock()
        return self._seat_mutexes[seat_id]

    def lock_seats(self, show: Show, seats: List[Seat], user: User):
        now = datetime.utcnow()
        # Sort to prevent deadlocks
        seats_sorted = sorted(seats, key=lambda s: s.id)

        # Acquire each seat's mutex
        for seat in seats_sorted:
            self._get_mutex(seat.id).acquire()

        try:
            show_locks = self.locks.setdefault(show.id, {})
            # Check for existing valid locks
            for seat in seats_sorted:
                entry = show_locks.get(seat.id)
                if entry and now < entry['expires_at']:
                    raise Exception(f"Seat {seat.id} is already locked.")
            # Place new locks
            for seat in seats_sorted:
                show_locks[seat.id] = {
                    'user_id': user.id,
                    'expires_at': now + self.timeout
                }
        finally:
            # Release all mutexes
            for seat in seats_sorted:
                self._get_mutex(seat.id).release()

    def unlock_seats(self, show: Show, seats: List[Seat], user: User):
        show_locks = self.locks.get(show.id, {})
        for seat in seats:
            if seat.id in show_locks and show_locks[seat.id]['user_id'] == user.id:
                del show_locks[seat.id]

    def validate_lock(self, show: Show, seat: Seat, user: User) -> bool:
        now = datetime.utcnow()
        entry = self.locks.get(show.id, {}).get(seat.id)
        return bool(entry and entry['user_id'] == user.id and now < entry['expires_at'])

    def get_locked_seats(self, show: Show) -> List[str]:
        now = datetime.utcnow()
        show_locks = self.locks.get(show.id, {})
        # Prune expired
        expired = [sid for sid, e in show_locks.items() if now >= e['expires_at']]
        for sid in expired:
            del show_locks[sid]
        return list(show_locks.keys())


# === Services ===

class MovieService:
    def __init__(self):
        self._movies: Dict[str, Movie] = {}

    def create(self, name: str, duration: int) -> Movie:
        m = Movie(name, duration)
        self._movies[m.id] = m
        return m

    def get(self, movie_id: str) -> Movie:
        return self._movies[movie_id]
    

class TheatreService:
    def __init__(self):
        self._screens: Dict[str, Screen] = {}

    def create_screen(self, name: str) -> Screen:
        s = Screen(name)
        self._screens[s.id] = s
        return s

    def get_screen(self, screen_id: str) -> Screen:
        return self._screens[screen_id]

class ShowService:
    def __init__(self):
        self._shows: Dict[str, Show] = {}

    def create(self, movie: Movie, screen: Screen, start_time: datetime) -> Show:
        show = Show(movie, screen, start_time)
        self._shows[show.id] = show
        return show

    def get(self, show_id: str) -> Show:
        return self._shows[show_id]


class BookingService:
    def __init__(self, lock_provider: SeatLockStategy):
        self._lock_provider = lock_provider
        self._bookings: Dict[str, Booking] = {}

    def create(self, user: User, show: Show, seats: List[Seat]) -> Booking:
        # ensure none are already confirmed
        confirmed = {
            s for b in self._bookings.values() if b.status is BookingStatus.CONFIRMED for s in b.seats
        }
        for seat in seats:
            if seat.id in confirmed:
                raise Exception(f"Seat {seat.id} already booked.")
        # lock and record
        self._lock_provider.lock_seats(show, seats, user)
        booking = Booking(user, show, seats)
        self._bookings[booking.id] = booking
        return booking

    def confirm(self, booking_id: str, user: User):
        booking = self._bookings[booking_id]
        if booking.user.id != user.id:
            raise Exception("Cannot confirm another user's booking")
        # validate locks
        for seat in booking.seats:
            if not self._lock_provider.validate_lock(booking.show, seat, user):
                raise Exception("Lock invalid or expired")
        booking.confirm()

    def get_booked_seats(self, show: Show) -> List[str]:
        return [
            seat.id
            for b in self._bookings.values()
            if b.show.id == show.id and b.status is BookingStatus.CONFIRMED
            for seat in b.seats
        ]

class SeatAvailabilityService:
    def __init__(self, booking_service: BookingService, lock_provider: SeatLockStategy):
        self.booking_service = booking_service
        self.lock_provider = lock_provider

    def get_available(self, show: Show) -> List[str]:
        all_seat_ids = [s.id for s in show.screen.seats]
        booked = set(self.booking_service.get_booked_seats(show))
        locked = set(self.lock_provider.get_locked_seats(show))
        unavailable = booked.union(locked)
        return [sid for sid in all_seat_ids if sid not in unavailable]
    


class PaymentStrategy:
    def process(self) -> bool:
        raise NotImplementedError


class DebitCardStrategy(PaymentStrategy):
    def process(self) -> bool:
        # simulate success
        return True


class UpiStrategy(PaymentStrategy):
    def process(self) -> bool:
        # simulate failure
        return False



class PaymentService:
    def __init__(self, strategy: PaymentStrategy, booking_service: BookingService):
        self.strategy = strategy
        self.booking_service = booking_service
        self.failures: Dict[str, int] = {}

    def pay(self, booking_id: str, user: User):
        if self.strategy.process():
            self.booking_service.confirm(booking_id, user)
        else:
            self.failures[booking_id] = self.failures.get(booking_id, 0) + 1
            print(f"Payment failed {self.failures[booking_id]} time(s) for {booking_id}")
# === Example Usage ===

if __name__ == "__main__":
    from datetime import datetime
    import threading

    # Initialize services
    mv_srv = MovieService()
    th_srv = TheatreService()
    show_srv = ShowService()
    lock_provider = InMemorySeatLockProvider(timeout_seconds=600)
    bk_srv = BookingService(lock_provider)
    avail_srv = SeatAvailabilityService(bk_srv, lock_provider)
    pay_srv = PaymentService(DebitCardStrategy(), bk_srv)

    # Create domain entities
    movie = mv_srv.create("Interstellar", 169)
    screen = th_srv.create_screen("IMAX Screen")
    # Add seats to the screen
    for row in range(1, 4):
        for _ in range(5):
            screen.add_seat(Seat(row, SeatCategory.GOLD))

    show = show_srv.create(movie, screen, datetime.utcnow())
    user1 = User("Alice", "alice@example.com")
    user2 = User("Bob", "bob@example.com")
    user3 = User("Tarang", "")

    available = avail_srv.get_available(show)
    print("Available seat IDs before booking:", available)

    # Helper for concurrent booking
    def attempt_booking(user, seat_indices):
        try:
            seats_to_book = [screen.seats[i] for i in seat_indices]
            booking = bk_srv.create(user, show, seats_to_book)
            print(f"{user.name} created booking {booking.id} for seats {[s.id for s in seats_to_book]}")
            pay_srv.pay(booking.id, user)
            status = bk_srv._bookings[booking.id].status
            print(f"{user.name}'s booking {booking.id} status: {status}")
        except Exception as e:
            print(f"{user.name} failed to book seats {[i+1 for i in seat_indices]}: {e}")

    # Simulate two users booking overlapping seats concurrently
    t1 = threading.Thread(target=attempt_booking, args=(user1, [0, 1, 2]))
    t2 = threading.Thread(target=attempt_booking, args=(user2, [3, 4]))
    t3 = threading.Thread(target=attempt_booking, args=(user3, [2,3, 4]))


    t3.start()
    t1.start()
    t2.start()
    t3.join()
    t1.join()
    t2.join()

    # Final available seats
    available = avail_srv.get_available(show)
    print("Final available seat IDs:", available)



