#User function Template for python3

class Solution:
    def getDayOfWeek(self, d, m, y):
        # code here 
        ans=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        t=[0,3,2,5,0,3,5,1,4,6,2,4]
        if m < 3 :
            y=y-1
        x=(y+ y//4 + y//400 - y//100 + t[m-1] + d)%7
        return ans[x]
