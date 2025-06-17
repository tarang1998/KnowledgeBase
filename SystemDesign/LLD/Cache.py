import threading 
from abc import ABC, abstractmethod
from collections import defaultdict
import time 
from concurrent.futures import ThreadPoolExecutor, Future


# Source of truth for your key→value mappings
class CacheStorage(ABC):
    @abstractmethod
    def put(self,key,value):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def contains_key(self, key) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def get_capacity(self)->bool:
        pass


class DBStorage(ABC):
    @abstractmethod
    def write(self,key, value):
        pass
    @abstractmethod
    def read(self, key):
        pass
    @abstractmethod
    def delete(self, key):
        pass


# Strategy Pattern 
class WritePolicy(ABC):
    @abstractmethod
    def write(self,key,value,cache_storage : CacheStorage, db_storage : DBStorage):
        pass


# Strategy Pattern
# bookkeeping for recency ordering—it only needs to know which keys were touched, and in what order.
class EvictionAlgorithm(ABC):
    @abstractmethod
    def key_accessed(self,key):
        pass
    @abstractmethod
    def evict_key(self):
        pass




class InMemoryCacheStorage(CacheStorage):
    def __init__(self, capacity: int, default_ttl: float = None):
        self._cache = dict()
        self._capacity = capacity
        self._lock = threading.Lock()
        self._default_ttl = default_ttl

    def put(self, key, value):
        with self.lock:
            expire_at = time.time() + self._default_ttl if self._default_ttl else None 
            self._cache[key] = (value, expire_at)

    def get(self, key):
        with self._lock: 
            if key not in self._cache:
                raise KeyError(f"Key not in cache: {key}")
            value, expire_at = self._cache[key]
            if expire_at and time.time() > expire_at:
                del self._cache[key]
                raise KeyError(f"Key expired: {key}")
            return value
    
    def remove(self, key):
        with self._lock:
            if key not in self._cache:
                raise KeyError(f"Key not in cache: {key}")
            del self._cache[key]

    def contains_key(self, key) -> bool:
        with self.lock:
            if key not in self._cache:
                return False
            value, expiresAt = self._cache[key]
            if expiresAt and time.time() + self._default_ttl> expiresAt:
                del self._cache[key]
                return False
            return True 
        
    def size(self) -> int:
        with self.lock:
            keys = list(self._cache.keys())
            for key in keys:
                value, expires_at = self._cache[key]
                if expires_at and time.time() + self._default_ttl > expires_at:
                    del self._cache[key]
            return len(self._cache)
        
    def get_capacity(self):
        return self.get_capacity
        
class SimpleDBStorage(DBStorage):
    def __init__(self):
        self._store = dict()
        self._lock = threading.Lock()

    def write(self, key, value):
        with self._lock:
            self._store[key] = value

    def read(self,key):
        with self._lock:
            if key not in self._store:
                raise KeyError(f"Key not found in DB: {key}")
            return self._store[key]
        
    def delete(self,key):
        with self._lock:
            if key not in self._store:
                raise KeyError(f"Key not found in DB: {key}")
            del self._store[key]

class WriteThroughPolicy(WritePolicy):
    def write(self,key,value,cache_storage: CacheStorage, db_storage: DBStorage):
        futs = []
        futs.append(ThreadPoolExecutor(max_workers=1).submit(cache_storage.put, key, value))
        futs.append(ThreadPoolExecutor(max_workers=1).submit(db_storage.write, key, value))
        for f in futs:
            f.result()

class _DLLNode: 
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self,node: _DLLNode):
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            node.next = None

    def remove(self, node : _DLLNode):
        if node.prev:
            node.prev.next = node.next 
        else:
            # Head is being removed
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = node.next = None 

    def remove_head(self) -> _DLLNode:
        if not self.head:
            return None 
        node = self.head
        self.remove(node)
        return node
    
class LRUEvictionAlgorithm(EvictionAlgorithm):
    def __init__(self):
        self._dll = DoublyLinkedList()
        self._map = dict()
        self._lock = threading.Lock()

    def key_accessed(self, key):
        with self._lock:
            if key in self._map:
                node = self._map[key]
                self._dll.remove(node)
                self._dll.add_to_tail(node)
            else:
                node = _DLLNode(key)
                self._dll.add_to_tail(node)
                self._map[key] = node

    def evict_key(self):
        with self._lock:
            node = self._dll.remove_head()
            if node is None:
                return None
            key = node.key
            del self._map[key]
            return key 


# === Key-Based Executor ===
class KeyBasedExecutor:
    def __init__(self, num_executors: int):
        self._executors = [ThreadPoolExecutor(max_workers=1) for _ in range(num_executors)]
        self._num = num_executors

    def submit_task(self, key, fn, *args, **kwargs) -> Future:
        idx = self._index_for_key(key)
        return self._executors[idx].submit(fn, *args, **kwargs)

    def _index_for_key(self, key) -> int:
        return abs(hash(key)) % self._num

    def shutdown(self):
        for ex in self._executors:
            ex.shutdown(wait=True)


# === Core Cache ===
# Facade Pattern 
# Dependency Injections
class Cache:
    def __init__(self, cache_storage: CacheStorage, db_storage: DBStorage,
                 write_policy: WritePolicy, eviction_algo: EvictionAlgorithm,
                 num_executors: int = 4):
        self._cache = cache_storage
        self._db = db_storage
        self._policy = write_policy
        self._evict = eviction_algo
        self._exec = KeyBasedExecutor(num_executors)
        self.hits = 0
        self.misses = 0

    def access_data(self, key) -> Future:
        def task():
            if self._cache.contains_key(key):
                self._evict.key_accessed(key)
                self.hits += 1
                return self._cache.get(key)
            else:
                self.misses += 1
                raise KeyError(f"Cache miss for key: {key}")
        return self._exec.submit_task(key, task)

    def update_data(self, key, value) -> Future:
        def task():
            if self._cache.contains_key(key):
                self._policy.write(key, value, self._cache, self._db)
                self._evict.key_accessed(key)
            else:
                if self._cache.size() >= self._cache.get_capacity():
                    evicted = self._evict.evict_key()
                    if evicted is not None:
                        # remove on its executor
                        self._exec.submit_task(evicted, self._cache.remove, evicted).result()
                self._policy.write(key, value, self._cache, self._db)
                self._evict.key_accessed(key)
        return self._exec.submit_task(key, task)

    def shutdown(self):
        self._exec.shutdown()


# === Example Usage ===
if __name__ == "__main__":
    cache = Cache(
        InMemoryCacheStorage(capacity=5, default_ttl=10),
        SimpleDBStorage(),
        WriteThroughPolicy(),
        LRUEvictionAlgorithm(),
        num_executors=4
    )

    # Populate cache
    for k, v in zip(['A','B','C','D','E'], ['Apple','Banana','Cherry','Durian','Elderberry']):
        cache.update_data(k, v).result()

    # Trigger eviction
    cache.update_data('F', 'Fig').result()

    # Access
    try:
        print(cache.access_data('A').result())
    except Exception as e:
        print(e)
    print(cache.access_data('F').result())

    cache.update_data('B', 'Blueberry').result()
    print(cache.access_data('B').result())

    print(f"Hits: {cache.hits}, Misses: {cache.misses}")

    cache.shutdown()
