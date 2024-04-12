#User function Template for python3

class Solution:
    def pairAndSum(self, n, arr):
        #code here
        sum=0
        #then we iterate through each bit position
        for i in range(32):
            #set bits refer to number of 1's in binary rep of integer
            #we are going to count the set bits at each position
            #inititally the count will be zero
            count=0
            #now we iterate through the array using j
            for j in arr:
                 # Check if the bit at position i is set (1) in the current element
                if j&(1<<i):
                    # Increment the count if the bit is set
                    count+=1
            #calculate the sum contributed by the bit position
            sum+=count*(count-1)//2*(1<<i)
        return sum

#001010
#010100
#011110
#101000

#16+24+4+2
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Arr=list(map(int,input().strip().split(' ')))
        ob=Solution()
        print(ob.pairAndSum(N,Arr))
# } Driver Code Ends