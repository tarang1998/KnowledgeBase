# Database Sharding 

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
