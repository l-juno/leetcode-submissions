class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keySet = dict()
        self.cache = []
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.remove(key)
            self.cache.append(key)
            return self.keySet[key]
        else:
            return -1
        
        
        

    def put(self, key: int, value: int) -> None:
        self.keySet[key] = value
        # check if exists in keySet
        if key in self.cache:
            self.cache.remove(key)
            self.cache.append(key)
        # check if full
        elif len(self.cache) >= self.capacity:
            self.cache.pop(0)
            self.cache.append(key)
        else:
            self.cache.append(key)
        print(self.cache)
        
        
            
        
