class Solution:
    def solve(self, a : int, b : int) -> int:
        # code here
        if a==b :
            return 0 
        if (((a&b)==a) or ((a&b)==b)) :
            return 1
        return 2



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.solve(a, b)
        
        print(res)
        

# } Driver Code Ends
