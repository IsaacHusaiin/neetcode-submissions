class MyHashMap:

    def __init__(self):
        self.buckets = [[] for _ in range(10)]

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[key %10]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))


    def get(self, key: int) -> int:
        bucket = self.buckets[key %10]
        for k, v in bucket:
            if k==key:
                return v
        return -1 
        

    def remove(self, key: int) -> None:
        bucket = self.buckets[key %10]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)