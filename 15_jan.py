from collections import defaultdict
class Solution():
    def countSubstring(self, S):
        #your code here
        x1=defaultdict(int)
        x2=defaultdict(int)
        count=0
        x1[0]=1
        x2[1]=1
        ans=0
        for i in S:
            if i=='1':
                ones = 1
            else:
                ones = -1
            count=count+ones
            x1[count] += 1+x2[count]
            x2[count+1] += 1+x2[count]
            x2[count]=0
            ans=ans+x1[count-1]
        return ans
