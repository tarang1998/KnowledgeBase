# ACID 

- Atomicity, Consistency, Isolation, Durability in relational Databases

## Transactions 

- A collection on queries 
- Its a one unit of work

## Atomicity 

- All queries in a transaction must succeed 
- If even one of the query fails, all the previous successfully queries should be rolled back 
- Lack of atomicity leads to inconsistency of the data

## Islolation

### Isolation-Read phenomena 

#### Dirty Reads 

- Consider 2 transaction T1 and T2 and Table Sales(PID,QNT,PRICE) with data [ (1,10,5), (2,20,4) ]:
- T1(1) : Select PID, QNT * PRICE From Sales 
- T1(2) : Select SUM(QNT * PRICE) From Sales 
- T2(1) : UPDATE SALES SET QNT = QNT + 5 WHERE PID = 1
- Order of execution : T1(1), T2(1), T1(2), T2(RollBack)
- TI(1) Reads : [ (1,50), (2,80) ]
- T2(1) Updates Row (1,10,5) => (1,15,5)
- T1(2) Reads a dirty value, The value set by T2(1) before T2 is committed
- For T1(2) We get the result as 155(15 * 5 + 20 * 4) when it should have been 130 (10 * 5 + 20 * 4) according to the values read by T1(1)
- This leads to an inconsistent results

#### Non-Repeatable Reads
- Consider 2 transaction T1 and T2 and Table Sales(PID,QNT,PRICE) with data [ (1,10,5), (2,20,4) ]:
- T1(1) : Select PID, QNT * PRICE From Sales
- T1(2) : Select SUM(QNT * PRICE) From Sales
- T2(1) : UPDATE SALES SET QNT = QNT + 5 WHERE PID = 1
- Order of execution : T1(1), T2(1), T2(Commit), T1(2)
- Over here T1(1) returns result : [ (1,50) , (2,80) ]
- T2(1) updates the value and commits : (1,10,5) => (1,15,5)
- T1(2) tries to read the updated value which was different from the initial value
- For T1(2) We get the result as 155(15 * 5 + 20 * 4) when it should have been 130 (10 * 5 + 20 * 4) according to the values read by T1(1)
- This leads to inconsistency 

#### Phantom Reads
- Consider 2 transaction T1 and T2 and Table Sales(PID,QNT,PRICE) with data [ (1,10,5), (2,20,4) ]:
- T1(1) : Select PID, QNT * PRICE From Sales
- T1(2) : Select SUM(QNT * PRICE) From Sales
- T2(1) : INSERT INTO SALES VALUES(3,10,1)
- Order of execution : T1(1), T2(1), T2(Commit), T1(2)
- Over here T1(1) returns result : [ (1,50) , (2,80) ]
- T2(1) inserts a row in the table (3,10,1)
- For T1(2) We get the result as 155(10 * 5 + 20 * 4 + 10 * 1) when it should have been 130 (10 * 5 + 20 * 4) according to the values read by T1(1)
- This leads to inconsistency

#### Lost Updates
- Consider 2 transaction T1 and T2 and Table Sales(PID,QNT,PRICE) with data [ (1,10,5), (2,20,4) ]:
- T1(1) : UPDATE SALES SET QNT = QNT + 10 WHERE PID = 1
- T1(2) : Select SUM(QNT * PRICE) From SALES
- T2(1) : UPDATE SALES SET QNT = QNT + 5 WHERE PID = 1
- Order of execution : T1(1), T2(1), T2(Commit), T1(2)
- T1(1) updates the row (1,10,5) => (1,20,5)
- T2(1) starts at the same time as T1(1) and updates the original value : (1,10,5) => (1,15,5). Here the update done by T1(1) is lost
- T1(2) returns result 155 ( 15 * 5 + 20 * 4) when it should have been 180 
- The update done by T1(1) was overwritten by another transaction.

### Isolation Levels for inflight transactions

- Isolation levels that were invented to fix the isolation-read phenomenon

#### Read Uncommitted 
- No isolation, any change from the outside is visible to the transaction, committed or not 
- This could lead to problems like Dirty Read, Non repeatable reads, phantom reads, lost updates

#### Read Committed
- Each query in a transaction only sees committed changes by other transactions
- This could also lead to problems like Non Repeatable reads, Phantom Reads, lost updates
- This is the default isolation level for many databases

#### Repeatable Read
- Invented to solve the problem of non repeatable reads
- The transaction will make sure that when a query reads a row, that row will remain unchanged while the transaction is running
- Phantom reads might still occur.

#### Snapshot 
- Each query in the transaction only sees changes that have been committed up to the start of the transaction
- Its like a snapshot version of the database at the moment 
- Solves all the isolation-read phenomenon but might be costly 

#### Serializable 
- Transactions are run in a serialized manner one after the another 
- Solves all the isolation-read phenomenon but might be costly, but might be slow


### DBMS Isolation Implementation
- Each DBMS Implements Isolation Levels Differently
- Pessimistic approach : Row level locks, table locks , page locks to avoid lost updates. This could be costly 
- Optimistic approach : No locks, just track if things changed and fail the transaction if so 
- Repeatable reads locks the rows it reads but it could be expensive if you read a lot of rows
- Postgress implements RR as a snapshot 
- That is why you dont get phantom reads with postgress in repeatable reads
- Serializable are usually implemented with optimistic concurrency control, you can implement it pessimistically with SELECT FOR UPDATE


## Consistency

### Consistency In Data
- Defined by the user(The DataBase Administrator)
- Comes down to enforcing referential integrity
- Atomicity ensures consistency in data
- Isolation could also result inconsistency


### Consistency In Read
- If a transaction commited a change will the new transaction immediately see the change. If not then that could lead to inconsistency
- Affects the system as a whole, incase of a master, replica architecture. If changes are made to the master but the changes haven't been propogated to the replicas and before that a read occurs from the replica. Inconsistent data is read in this case.
- Relational and NoSQL Databases suffer from this
- Eventual Consistency can be reached after some time 

## Durability
- Changes made by the committed transaction must be persisted in a durable non-volatile storage

