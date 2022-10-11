# Caching 

- A cache is a hardware or a software that you use to temporarily store data so it can be accessed quickly
- Caches take advantage of the locality of reference principle : recently requested data is likely to be requested again.
- If the required data is found in the Cache it is called a **Cache Hit**. If the data isn't stored in the cache, a **Cache Miss** occurs.
- The different types of caching stratergies are : 

    - **Cache Invalidation**

        - It is a process in which the system declares cache entries as invalid and either removes them or replaces them.
        - The basic objective of the process is to ensure that when client request the data, the latest version of the data is returned.
        - Three main schemes are used 
            - Write-through cache 
                - 

    - **Cache Eviction**


## Resources

- [Caching | Cache Patterns | Cache Invalidation & Eviction](https://www.youtube.com/watch?v=Ez1GK2imrsY)
- [System Design: Why is single-threaded Redis so fast?](https://www.youtube.com/watch?v=5TRFpFBccQM&list=PLCRMIe5FDPse7NNmQP5UziLjXjkHW3gqA)