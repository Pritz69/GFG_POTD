#User function Template for python3

class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self, s, k):
        #code here

        ans = '0'
        n = len(s)
        def change(l, i, k, ident = 0):
            nonlocal ans, n
            if k == 0 or i >= n:
                ans = max(ans, "".join(l))
                return
                
            m, pos = '0', []
            for j in range(i, n):
                if l[j] == m:
                    pos.append(j)
                elif l[j] > m:
                    m = l[j]
                    pos = [j]
                
            for j in pos:
                if j == i:
                    change(l, i+1, k, ident+1)
                else:
                    l[i], l[j] = l[j], l[i]
                    change(l, i+1, k-1, ident+1)
                    l[i], l[j] = l[j], l[i]
            
        change(list(s), 0, k)
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob = Solution()
        print(ob.findMaximumNum(s, k))

        print("~")

# } Driver Code Ends