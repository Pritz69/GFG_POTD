#User function Template for python3
class Solution:
    def findOrder(words):
        # code here
        from collections import defaultdict
        from itertools import product
        
        g = defaultdict(set)
        n = len(words)
        chars = set(words[-1])
        for i in range(n-1):
            chars.update(words[i])
            for j in range(i+1, n):
                w1, w2 = words[i], words[j]
                for k in range(min(len(w1), len(w2))):
                    if w1[k] != w2[k]:
                        g[w1[k]].add(w2[k])
                        break
                else:
                    if len(w1) > len(w2):
                        return ""
                
        
        visited, on_stack = set(), set()
        result = []
        
        def dfs(n):
            if n in on_stack:
                return True 
            if n in visited:
                return False
            
            on_stack.add(n)
            for nbr in g.get(n, []):
                if dfs(nbr):
                    return True
            on_stack.remove(n)
            visited.add(n)
            result.append(n)
            
        for n in g.keys():
            if n not in visited:
                if dfs(n):
                    return ""
 
        result.extend(chars - set(result))
        return "".join(reversed(result))

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
from collections import deque

#Position this line where user code will be pasted.


def validate(original, order):
    char_map = {}
    for word in original:
        for ch in word:
            char_map[ch] = 1

    for ch in order:
        if ch not in char_map:
            return False
        del char_map[ch]

    if char_map:
        return False

    char_index = {ch: i for i, ch in enumerate(order)}

    for i in range(len(original) - 1):
        a, b = original[i], original[i + 1]
        k, n, m = 0, len(a), len(b)
        while k < n and k < m and a[k] == b[k]:
            k += 1
        if k < n and k < m and char_index[a[k]] > char_index[b[k]]:
            return False
        if k != n and k == m:
            return False

    return True


if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split("\n")
    index = 0
    t = int(input_data[index])
    index += 1
    while t > 0:
        words = input_data[index].split()
        index += 1
        original = words[:]

        order = Solution.findOrder(words)

        if order == "":
            print("\"\"")
        else:
            print("true" if validate(original, order) else "false")
        print("~")
        t -= 1

# } Driver Code Ends