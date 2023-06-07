#User function Template for python3
import math
class Solution:
    def leastPrimeFactor (self, n):
        # code here 
        l=[0]*(n+1)
        l[1]=1
        for i in range(2,n+1) :
            l[i] = i
        for i in range(2,int(math.sqrt(n))+1) :
            if l[i]==i :
                for j in range(i*i ,n+1 ,i) :
                    if l[j]==j :
                        l[j]=i
        return l
        
