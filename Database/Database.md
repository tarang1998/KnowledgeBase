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

- Consider 2 transaction T1 and T2 and Table Sales(PID,QNT,PRICE) with data [ (1,10,5), (1,20,4) ]:
- T1(1) : Select PID, QNT * PRICE From Sales
- T1(2) : Select SUM(QNT * PRICE) From Sales
- T2(1) : UPDATE SALES SET QNT = QNT + 5 WHERE PID = 1
- Order of execution : T1(1), T2(1), T1(2), T2(RollBack)
- TI(1) Reads : [ (1,10,5), (1,20,4) ]
- T1(2) Reads a dirty value, The value set by T2(1) before T2 is committed
- For T1(2) We get the result as 155(15 * 5+ 20 * 4) when it should have been 130 (10 * 5 + 20 * 4)


- Non-Repeatable Reads
- Phantom Reads
- Lost Updates 