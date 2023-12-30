#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        d={}
        for x in arr :
            d[x]=d.get(x,0)+1
        ans=""
        d=dict(sorted(d.items()))
        #print(d)
        l=[]
        m=0
        for x in d :
            if d[x]  > m :
                m=d[x]
        for x in d :
            if d[x]==m :
                l.append(x)
        return [min(l),m]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends