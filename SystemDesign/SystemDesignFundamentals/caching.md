# Caching 

- A cache is a hardware or a software that you use to temporarily store data so it can be accessed quickly
- Caches take advantage of the locality of reference principle : recently requested data is likely to be requested again.
- If the required data is found in the Cache it is called a **Cache Hit**. If the data isn't stored in the cache, a **Cache Miss** occurs.
- The different types of caching stratergies are : 

    - **Cache Invalidation**

        - It is a process in which the system declares cache entries as invalid and either removes them or replaces them.
        - The basic objective of the process is to ensure that when client request the data, the latest version of the data is returned.
        - Three main schemes are used :

            - Write through cache 
                - The data is written in the cache and the corresponding disk simultaneously.
                - Ensures data consistency and reliability but results in high latency for write operations as every write operation is done twice.

            - Write around cache
                - The data is written directly to permenant storage, bypassing the cache.
                - Cache wont be flooded with write request that may not be subsequently re-read.
                - If the read request arises for the data recently written it will lead to a cache miss resulting in higher latency

            - Write back cache 
                - Data is written in the cache alone and completion is immediately confirmed to the client.
                - The write to permenant storage is done at a specific interval or under certain conditions.
                - Results in low latency and high throughput for write itensive applications.
                - There is a risk of data loss in case of a crash

    - **Cache Eviction**


## Resources

- [Caching | Cache Patterns | Cache Invalidation & Eviction](https://www.youtube.com/watch?v=Ez1GK2imrsY)
- [System Design: Why is single-threaded Redis so fast?](https://www.youtube.com/watch?v=5TRFpFBccQM&list=PLCRMIe5FDPse7NNmQP5UziLjXjkHW3gqA)