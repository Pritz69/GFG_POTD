
class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        d={}
        for x in s :
            d[x]=d.get(x,0)+1
        o,e=0,0
        for x in d :
            if d[x]%2==1 and ord(x) %2==1 :
                o +=1
            elif d[x]%2==0 and ord(x) %2==0:
                e +=1
        if (o+e)%2 ==1 :
            return "ODD" 
        else :
            return "EVEN"



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends