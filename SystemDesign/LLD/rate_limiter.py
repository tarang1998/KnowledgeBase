import threading
import time
from typing import Optional, Dict
from concurrent.futures import ThreadPoolExecutor, Future


class IRateLimiter:
    def give_access(self, rate_limit_key: Optional[str]) -> bool:
        raise NotImplementedError

    def update_configuration(self, config: Dict[str, any]) -> None:
        raise NotImplementedError

    def shutdown(self) -> None:
        raise NotImplementedError


class TokenBucketStrategy(IRateLimiter):
    class Bucket:
        def __init__(self, capacity: int, refresh_rate: int):
            self.capacity = capacity
            self.refresh_rate = refresh_rate
            self.tokens = capacity
            self.lock = threading.Lock()

        def try_consume(self) -> bool:
            with self.lock:
                if self.tokens > 0:
                    self.tokens -= 1
                    return True
                return False

        def refill(self):
            with self.lock:
                self.tokens = min(self.capacity, self.tokens + self.refresh_rate)

    def __init__(self, capacity: int, refresh_rate: int):
        self.capacity = capacity
        self.refresh_rate = refresh_rate
        self.global_bucket = self.Bucket(capacity, refresh_rate)
        self.user_buckets: Dict[str, TokenBucketStrategy.Bucket] = {}
        self.bucket_lock = threading.Lock()
        self.shutdown_event = threading.Event()
        self.refill_thread = threading.Thread(target=self._refill_task, daemon=True)
        self.refill_thread.start()

    def _refill_task(self):
        while not self.shutdown_event.is_set():
            self.global_bucket.refill()
            with self.bucket_lock:
                for bucket in self.user_buckets.values():
                    bucket.refill()
            time.sleep(1)

    def give_access(self, rate_limit_key: Optional[str]) -> bool:
        if rate_limit_key:
            with self.bucket_lock:
                bucket = self.user_buckets.setdefault(
                    rate_limit_key, self.Bucket(self.capacity, self.refresh_rate))
            return bucket.try_consume()
        return self.global_bucket.try_consume()

    def update_configuration(self, config: Dict[str, any]) -> None:
        if 'refresh_rate' in config:
            self.refresh_rate = config['refresh_rate']
            self.global_bucket.refresh_rate = self.refresh_rate
            with self.bucket_lock:
                for bucket in self.user_buckets.values():
                    bucket.refresh_rate = self.refresh_rate

    def shutdown(self) -> None:
        self.shutdown_event.set()
        self.refill_thread.join()


class RateLimiterFactory:
    @staticmethod
    def create_limiter(limiter_type: str, config: Dict[str, any]) -> IRateLimiter:
        if limiter_type == "TOKEN_BUCKET":
            capacity = config.get("capacity", 10)
            refresh_rate = config.get("refresh_rate", 1)
            return TokenBucketStrategy(capacity, refresh_rate)
        raise ValueError(f"Unsupported rate limiter type: {limiter_type}")


class RateLimiterController:
    def __init__(self, limiter_type: str, config: Dict[str, any], max_workers: int = 10):
        self.rate_limiter = RateLimiterFactory.create_limiter(limiter_type, config)
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def process_request(self, rate_limit_key: Optional[str]) -> Future:
        return self.executor.submit(self.rate_limiter.give_access, rate_limit_key)

    def update_configuration(self, config: Dict[str, any]) -> None:
        self.rate_limiter.update_configuration(config)

    def shutdown(self) -> None:
        self.rate_limiter.shutdown()
        self.executor.shutdown(wait=True)


if __name__ == "__main__":
    config = {"capacity": 5, "refresh_rate": 2}
    controller = RateLimiterController("TOKEN_BUCKET", config)

    for i in range(10):
        future = controller.process_request("user1")
        allowed = future.result()
        print(f"Request {i+1}: {'✅ Allowed' if allowed else '❌ Blocked'}")
        time.sleep(0.2)

    controller.shutdown()
