# 🌈 The Enchanted Hash Table Realm 🍭

## 🦄 What Are Hash Tables?
Hash Tables are magical dictionaries that store key-value pairs with lightning-fast retrieval - like a wizard's spellbook where each spell is instantly findable!

## 🌸 Basic Hash Table Implementation

### 📦 Simple Hash Table Class
```python
class MagicalHashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        """Convert key to a hash index"""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair"""
        index = self._hash_function(key)
        
        # Check if key already exists
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        
        # Add new key-value pair
        self.table[index].append([key, value])

    def get(self, key):
        """Retrieve value by key"""
        index = self._hash_function(key)
        
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        
        raise KeyError(f"🌟 Magical key '{key}' not found!")

    def remove(self, key):
        """Remove a key-value pair"""
        index = self._hash_function(key)
        
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return
        
        raise KeyError(f"🌈 Magical key '{key}' not found!")
```

## 🍭 Collision Resolution Techniques

### 🌺 Chaining Method
```python
def insert_with_chaining(self, key, value):
    index = self._hash_function(key)
    
    # If no chain exists, create one
    if not self.table[index]:
        self.table[index] = []
    
    # Check for existing key
    for item in self.table[index]:
        if item[0] == key:
            item[1] = value
            return
    
    # Add new key-value pair
    self.table[index].append([key, value])
```

### 🦄 Open Addressing (Linear Probing)
```python
class LinearProbingHashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size
        self.occupied = 0

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        if self.occupied >= self.size * 0.7:
            self._resize()
        
        index = self._hash_function(key)
        
        while self.table[index] is not None:
            # If key already exists, update value
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            
            # Linear probing
            index = (index + 1) % self.size
        
        # Insert new key-value pair
        self.table[index] = (key, value)
        self.occupied += 1

    def _resize(self):
        """Resize the hash table when it gets too full"""
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.occupied = 0
        
        for item in old_table:
            if item is not None:
                self.insert(item[0], item[1])
```

## 💖 Advanced Hash Table Techniques

### 🌈 Implementing a Cache
```python
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.lru_order = []

    def get(self, key):
        if key not in self.cache:
            return -1
        
        # Move the accessed key to the end (most recently used)
        self.lru_order.remove(key)
        self.lru_order.append(key)
        
        return self.cache[key]

    def put(self, key, value):
        # If key already exists, update and move to end
        if key in self.cache:
            self.lru_order.remove(key)
        
        # If cache is full, remove the least recently used item
        elif len(self.cache) >= self.capacity:
            oldest = self.lru_order.pop(0)
            del self.cache[oldest]
        
        # Add new key
        self.cache[key] = value
        self.lru_order.append(key)
```

## 🌺 Real-World Hash Table Applications
- Caching mechanisms
- Database indexing
- Symbol tables in compilers
- Implementing dictionaries
- Unique data tracking

## 🦋 Wisdom of the Hash Table Realm
> "In the magical world of data, a Hash Table is like a librarian who knows exactly where every book is!" 

## 🍭 Practice Challenges
- [ ] Implement a custom hash function
- [ ] Create a spell-checking dictionary
- [ ] Design a simple cache system
- [ ] Build a frequency counter

## 💖 Motivational Corner
Remember, brave code explorer:
- Each key is a treasure
- Every hash is a shortcut
- Collisions are just puzzles waiting to be solved

Keep hashing, keep learning! 🌈✨