#implementing HashTable using linear probing mechanism 
#every function will eun in O(1)
class HashTable:
    def __init__(self):
        self.size = 5   #int(input("enter your desired size for table:"))
        self.arr = [None for i in range(self.size)]
        self.bucket = [None]*self.size
        self.keys=[]
        self.values=[]
        self.next = 0
        
    
    #hash function that will return a index value
    def __hashed(self, k):
        hash = 0
        for char in k:
            hash += ord(char) #taking sum of the the ascii value of the key's charatcters
        return hash % self.size #then take % of sum with the size of given array 
    
    
    #hashing the key again using linear probing method to avoid collisions if there are any.
    def Re_Hash(self,key):
        rehash = (key+1) % self.size   
        return rehash
    
    
    #by using hashed key insert key and value at the index we got
    def Insert(self, k, v):
        if self.next==self.size:  #if size of array is equal to the next that means array is overflow 
            return "Array is over flow" #return exception that array is over flow
        hashed_key = self.__hashed(k)   #store hashed key in a variable
        if self.bucket[hashed_key] == None:  #if index of array is equal to null
            self.arr[hashed_key]=k
            self.bucket[hashed_key]= v
            self.next=self.next+1 #incrementing next
            self.keys.append(k)  #add given key(k) to the keys list
            self.values.append(v)  ##add given value(v) to the value list
            return self.bucket
        else:
            hashed_key=self.Re_Hash(hashed_key)  #else re hash the key using Re_Hash function and store it in hashed_key.
             
            while self.arr[hashed_key] !=None: 
                hashed_key=self.Re_Hash(hashed_key)
            self.arr[hashed_key]=k
            self.bucket[hashed_key]= v
            self.next=self.next+1
            return  self.bucket 
        
        
    #this function will retrieve the given keys value from the table
    def Search_value(self, k):
        hashed_key = self.__hashed(k) #calculating the key by hash function 
        return self.bucket[hashed_key] #return the value
    
    
    def Remove(self, k):
        hashed_key = self.__hashed(k) #calculating the key by hash function 
        if self.bucket[hashed_key] is None: #check by if condition that index is already none
            print("key not found") #then print exception key not found
            
        else:
            self.bucket[hashed_key]=None #else set it to null
        
        
    #returns all keys in a list
    def Keys(self):
        return self.keys
    
    
    #returns all values in a list
    def Values(self):
        return self.values
    
    
    #returns key value pairs in tuple inside list
    def Entries(self):
        for key,value in zip(self.keys,self.values): #iterate through the keys and valuess list then with zip() function returns a zip object.
            print([(key,value)]) #print key,value pairs in tuple inside a list


    #returns the number of elements inserted 
    def Size(self):
        return len(self.keys) #return size by calculating the length of keys using len() 


    #returns True if the hashtable is empty else returns False
    def IsEmpty(self):
        if len(self.keys) == 0: #checks if len of keys is equal to 0
            return True #if True then its an underflow
        else:
            return False #otherwise return false
        
    #returns True if the hashtable is Full else returns False    
    def IsFull(self):
        if len(self.keys) >= self.size: #checks if len of keys is equal to or greater than the given size of table
            return True #if True then its a overflow
        else:
            return False  #otherwise return false
        
    
        
h = HashTable()
print(h.Insert("ironman",2))
print(h.Insert("thor",3))
print(h.Insert("blackwidow",5))
print(h.Insert("hort",6))
print(h.Remove("hort"))
print("Search value: ",h.Search_value("ironman"))
print("Keys: ",h.Keys())
print("Values: ",h.Values())
print("Entries: ")
print(h.Entries())
print("number of elements: ",h.Size())
print("Table is Empty: ",h.IsEmpty())
print("Table is Full: ",h.IsFull())
    