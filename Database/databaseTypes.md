# Database Types 

- Key Value Database 
    - Used for storing key value pair in a distributed manner
    - Amazon Dynamo DB, Redis, Cassandra

- Document based Databases 
    - Used when you are not sure about the structure of the data and how it is going to evolve
    - Used for storing JSON documents
    - Supports heavy read and write operations
    - ACID properties are not supported 
    - Data may contain Null values and they have to handled in the application code
    - Eg: Firebase, MongoDB, Azure CosmosDB, Couch DB

- Column Databases
    - Midway of relational DB's and document type DB's
    - There is a fixed Schema 
    - Does not support ACID properties 
    - Used when there is a requirement of heavy writes like streaming data, event data like Music Apps , iOT devices , health tracking apps 
    - Supports special type of reads
    - Good supporter of distributed databases 
    - Eg: Cassandra, HBase

- Search Databases 
    - The data stored in these databases is not the primary data source
    - Eg : Elastic , Solar

- Graph Database 
    - Used for storing data with complex relationships
    - Eg: Amazon Neptune, Neo4J, Tiger DB

- Ledger Database 
    - Store using an append only record journal
    - Amazon QLDB

- Distributed Data Processing System
    - Apache Hadoop/Spark




## Resources 

- [Databases types: SQL, NoSQL, Column, Search, Key Value ](https://www.youtube.com/watch?v=O_c7lzNbcKo&t=610s)
- [Types of Databases](https://www.bitdegree.org/tutorials/types-of-databases/)

## Questions 

- Which Database would you use to implement an real time voting system