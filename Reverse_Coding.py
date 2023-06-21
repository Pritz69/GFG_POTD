
class Solution:
    def sumOfNaturals(self, n):
        # code here 
        return ((n*(n+1))//2)%((10 **9)+7)
