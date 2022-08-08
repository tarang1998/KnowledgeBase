# System Design

## Concepts 

### Database Sharding 

- Data can be partitioned in two ways : Horizontal partitioning and Vertical partitioning
    - In horizontal partitioning data is partitioned on the basis of rows
    - In vertical partitioning data is partitioned on the basis of columns 
- Horizontal Partitioning is also known as sharding 
- Advantanges of sharding 
    - It reduces latency hence better performance
    - The conditional of single point of failure is avoided if the database is physically sharded
- Drawbacks of sharding
    - Could lead an overloaded data partition if the key is not choosen properly, thereby creating hotspots.
    - Its very difficult to revert the database from a sharded to a non-sharded architecture
    - Data Join operations are complex - cases in which data belongs to different shards



#### Resourcses
- [What is Database Sharding, Logical and Physical Shards, Dynamic vs Algorithmic Sharding](https://www.youtube.com/watch?v=YCb-tDQWrXk)
- [What is database sharding](https://www.youtube.com/watch?v=5faMjKuB9bc&list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX&index=7)


### API Rate Limiter

- 429 is the error code that is used which indicated that too may request were made
- [What are the different API rate limiting methods needed while designing large scale systems & why?](https://www.youtube.com/watch?v=YSW3UE5AFD4)
- [System Design Interview - Rate Limiting (local and distributed)](https://www.youtube.com/watch?v=FU4WlwfS3G0)

## System Designs Questions

- [UBER System Design](https://medium.com/@narengowda/uber-system-design-8b2bc95e2cfe)
- [UBER System design | OLA system design | uber architecture | amazon interview question](https://www.youtube.com/watch?v=umWABit-wbk)

## Articles

- [Difference between High Level Design and Low Level Design](https://www.geeksforgeeks.org/difference-between-high-level-design-and-low-level-design/)

- [Grokking the Object Oriented Design Interview](https://github.com/tssovi/grokking-the-object-oriented-design-interview)

## Videos 

- [System Design Basics Playlist](https://www.youtube.com/watch?v=xpDnVSmNFX0&list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX)

    - Horizontal and Vertical Scaling 
        - In the vertical scaling approach the computational power of the server is increased
        - In horizontal scaling the no of servers are increased

        - Horizontal Scaling 
            - Load Balancing is Required 
            - Network Calls (RPC) are involved 

        - Vertical Scaling 
            - Chances for a single point of failure
            - Inter process communication
            - Limited by hardware 


    - [Load Balancing](https://www.youtube.com/watch?v=K0Ta65OqQkY&list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX&index=3)

    - [Consistent Hashing](https://www.youtube.com/watch?v=zaRkONvyGr8&list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX&index=4)

    - [Messaging queue / Task Queue](https://www.youtube.com/watch?v=oUJbuFMyBDk&list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX&index=5)
 