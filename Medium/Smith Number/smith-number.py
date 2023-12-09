#User function Template for python3
from math import sqrt
class Solution:
    def smithNum(self, n):
        # code here 
        
        t=n
        def isprime(x) :
            if x==1 :
                return False
            if x==2 or x==3 :
                return True
            for i in range(2,int(sqrt(x))+2) :
                if x%i==0 :
                    return False
            return True
        
        if isprime(n):
            return 0
            
        s=0
        while n >0 :
            s += n%10
            n =n//10
        p=0
        i=2
        while t>1:
            if isprime(i) :
                while t>1 and t%i==0:
                    #print(i)
                    c=i
                    while c>0 :
                        p += c%10
                        c=c//10
                    t=t//i
            i +=1
        #print(p,s)
        return 1 if p==s else 0
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        
        ob = Solution()
        print(ob.smithNum(n))
# } Driver Code Ends