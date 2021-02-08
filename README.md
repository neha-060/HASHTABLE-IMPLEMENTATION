# HASHTABLE-IMPLEMENTATION
Hashtable Implementation using linear probing

HASHTABLE 
Hashtable is basically a data structure that stores key-value pairs and the place of storage is calculated using the key and a hash function. It is implementation of MAP ADT.
Functions used in HASHTABLE:
class HashTable:
def __hashed(self, k):
Sum the ASCII value of the characters and take the mode of sum with the size of array.
def Re_Hash(self,k):
Linear probing to avoid collision.
def Insert(self, k, v):
Insert we calculate a place of storage and then insert the value at that place in a hashtable.
def Search_value(self, k):
In search we retrieve the entry from the hashtable.
def Remove(self, k):
In delete operation we calculate the key and set it to null.
def Keys(self):
The keys of the dictionary are hashable i.e. they are generated by hashing function which generates unique result for each unique value supplied to the hash function.
def Values(self):
Hashing key to obtain its index value.
def Entries(self):
Taking key and value and print them.
def Size(self):
Return key length that is actually size.
def IsEmpty(self):
if len(self.keys) == 0:
            return True #underflow
        else:
            return False
def IsFull(self):
if len(self.keys) >= self.size:
            return True#overflow
        else:
            return False
