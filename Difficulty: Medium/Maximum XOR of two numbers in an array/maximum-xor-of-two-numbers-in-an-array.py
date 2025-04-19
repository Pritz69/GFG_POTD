#User function Template for python3

class TrieNode:
    def __init__(self):
        self.children = {}
class Solution:
    def insert(self, root, num):
        node = root
        for i in range(31, -1, -1):  # 32 bits (from MSB to LSB)
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    def maxXor(self, arr):
        root = TrieNode()
        
        # Step 1: Insert all numbers into Trie
        for num in arr:
            self.insert(root, num)

        max_xor = 0

        # Step 2: Find max XOR for each number
        for num in arr:
            node = root
            curr_xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                opposite_bit = 1 - bit
                if opposite_bit in node.children:
                    curr_xor |= (1 << i)
                    node = node.children[opposite_bit]
                else:
                    node = node.children.get(bit, node)
            max_xor = max(max_xor, curr_xor)

        return max_xor

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxXor(arr))
        print("~")

# } Driver Code Ends