#User function Template for python3
class Solution:
    def kPangram(self,string, k):
    # code here
        
        d={}
        for x in "abcdefghijklmnopqrstuvwxyz" :
            d[x]=d.get(x,0)
        s=0
        for x in string :
            if x==" " :
                continue
            d[x]=d.get(x,0)+1
            s +=1
        #print(len(d))
        if s < 26 :
            return False
        f=0
        c=0
        for x in d :
            if d[x] ==0 :
                f=1
                c +=1
        if f==0 :
            return True
        if c > k :
            return False
        else :
            return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends