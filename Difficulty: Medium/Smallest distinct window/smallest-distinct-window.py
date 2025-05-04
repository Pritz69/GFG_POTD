#User function Template for python3

class Solution:
    def findSubString(self, st):
        # code here
        ans=len(st)
        s=set(st)
        n=len(s)
        l,r=0,0
        d={}
        while r < len(st) :
            d[st[r]]=d.get(st[r],0)+1
            while len(d) == n :
                d[st[l]]=d[st[l]]-1
                if d[st[l]]==0 :
                    d.pop(st[l])
                ans=min(ans,(r-l)+1)
                l +=1
            r +=1
        return ans
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):
        str = input()
        ob = Solution()
        print(ob.findSubString(str))

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends