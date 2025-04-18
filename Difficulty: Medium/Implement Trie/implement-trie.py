#User function Template for python3
class Trie:
    def __init__(self):
        # implement Trie
        self.alphas = [None] * 26
        self.end = False
        
    def insert(self, word: str):
        node = self
        for ch in word:
            c = ord(ch) - ord('a')
            if node.alphas[c] == None:
                node.alphas[c] = Trie()
            node = node.alphas[c]
        node.end = True
        

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            c = ord(ch) - ord('a')
            if node == None:
                return False
            node = node.alphas[c]
            
        return node and node.end
        

    def isPrefix(self, word: str) -> bool:
        node = self
        for ch in word:
            if node == None:
                return False
            c = ord(ch) - ord('a')
            node = node.alphas[c]
            
        return node != None

#{ 
 # Driver Code Starts
def main():
    t = int(input())
    for _ in range(t):
        q = int(input())
        ans = []
        trie = Trie()

        for _ in range(q):
            x, s = input().split()
            x = int(x)

            if x == 1:
                trie.insert(s)
            elif x == 2:
                ans.append(trie.search(s))
            elif x == 3:
                ans.append(trie.isPrefix(s))

        # Print results as lowercase true/false
        print(" ".join(["true" if res else "false" for res in ans]))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends