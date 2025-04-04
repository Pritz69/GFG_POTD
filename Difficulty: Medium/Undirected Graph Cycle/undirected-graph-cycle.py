
class Solution:
	def isCycle(self, V, edges):
		#Code here
        p = [e for e in range(V+1)]
        
        def find(v):
            if p[v] != v:
                p[v] = find(p[v])
            return p[v]
        
        for u, v in edges:
            r1 = find(u)
            r2 = find(v)
            if r1 == r2:
                return True
            p[r1] = r2
        
        return False

#{ 
 # Driver Code Starts
import sys
#Position this line where user code will be pasted.


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))

        obj = Solution()
        ans = obj.isCycle(V, edges)
        print("true" if ans else "false")
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends