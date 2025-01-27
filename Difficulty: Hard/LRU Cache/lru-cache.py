#User function Template for python3

# design the class in the most optimal way

class LRUCache:
    
    def __init__(self, cap):
        self.cache = {}  # Normal dictionary instead of OrderedDict
        self.capacity = cap

    def get(self, key):
        if key in self.cache:
            # Move the accessed key to the end to mark it as recently used
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            # Update the value and move the key to the end
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Remove the least recently used item (first item in dictionary)
            self.cache.pop(next(iter(self.cache)))
        # Add the new key-value pair
        self.cache[key] = value

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def inputLine():
    return input().strip().split()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        capacity = int(input())
        cache = LRUCache(capacity)

        queries = int(input())
        for __ in range(queries):
            vec = inputLine()
            if vec[0] == "PUT":
                key = int(vec[1])
                value = int(vec[2])
                cache.put(key, value)
            else:
                key = int(vec[1])
                print(cache.get(key), end=" ")
        print()
        print("~")

# } Driver Code Ends