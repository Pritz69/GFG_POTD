#User function Template for python3

class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        ans=[]
        for x in intervals :
            if not ans or ans[-1][1] < x[0] :
                ans.append(x)
            else :
                ans[-1][1]=max(ans[-1][1],x[1])
        return ans
