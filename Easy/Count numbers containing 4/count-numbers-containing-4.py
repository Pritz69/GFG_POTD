
class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        def fornot(n) :
            while n > 0 :
                d= n%10
                if d==4 :
                    return True
                n= n//10
            return False
        c=0
        i=0
        while (i <= n) :
            if fornot(i) :
                c +=1
            
            i +=1
        return c

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.countNumberswith4(n)

        print(res)

# } Driver Code Ends