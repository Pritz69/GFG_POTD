class Solution:
    def lcmTriplets(self,N):
        #code here
        if N<=2:
            return N
        if (N%2)==1:
            return N*(N-1)*(N-2)
        if N%3==0:
            return (N-2)*(N-1)*(N-3)
        return N*(N-1)*(N-3)
