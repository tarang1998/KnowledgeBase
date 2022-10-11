
# HashMap

- Bucket is one element of the hashmap array. It can be used to store nodes. In the case a bucket has two or more nodes a linked list like structure can be used to connect the nodes. 

- Nodes in a hashmap can be represented by a class having the following objects : 
    - int hash : Holds the hash code of the key and it is final 
    - K key : It stores the key of the element and its final, it cannot be changed.
    - V value : It holds the value of the element, 
    - Node next : Holds the pointer to the next key-value pair. Initially it is null and gets a link in case of a hash collision

- Hashing is the process of converting an object into an integer form by using a hash function.(This function should be written properly for the better performance of HashMap and better utilization of the buckets.)
- Index calculation in a hashmap = hashCode(key) & (n-1) where n is the size of the bucket
- Incase after index calculation if the selected bucket already has a node an collision has occured. Check the key, if the key is the same replace the value else this node is connected to the previous node via the linked list. 
- It gives almost constant time performance of O(1) for put and get operations.
- The initial capacity of the hashMap is the capacity of the hashmap at the time of its creation (The no of buckets in the hashMap). The default value is 16 and it is doubled each time it reaches a threshold.
- Load factor is the measure which decides when to increase the capacity of the HashMap. Defaut value is 0.75f
- Threshold = Current Capacity * Load Factor , Eg : (16*0.75) = 12. This means the capacity is increased from 16 to 32 after the 12th element is added in the hashMap.
- Whenenever HashMap reaches a threshold, rehashing takes place




## Resources 

- [Internal Working of a Hashmap](https://www.geeksforgeeks.org/internal-working-of-hashmap-java/)
- [Working of HashMap in Java](https://www.linkedin.com/pulse/hashmap-jyoti-jindal/)

## Problems

- Ransom Note [[Problem Statement](https://leetcode.com/problems/ransom-note/) | [Python Solution](/CompetitiveProgramming/DictionariesAndHashMaps/RansomNote.py)] <sub> (Diff : Easy, Topics : HashTable, Counting, Sorting  )</sub> 

---
