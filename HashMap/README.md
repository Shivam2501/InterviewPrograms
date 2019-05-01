> KPCB Engineering Fellow Program
> Created by: Shivam Bharuka
> Contact: bharuka2@illinois.edu

Problem Statement:
Using only primitive types, implement a fixed-size 
hash map that associates string keys with arbitrary 
data object references.

Solution:
Implement a chained linked list fixed size hashMap
where each index of the map stores a linked list
of items with the same hash value to avoid collision.

```
Main file: KPCBMap.py
Unit tests: KPCBMapTests.py
```