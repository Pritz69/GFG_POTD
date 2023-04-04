class Solution:
    def minSteps(self, str : str) -> int:
        # code here
        a,b=0,0
        if str[0]=='a' :
            a +=1
        else :
            b +=1
        for i in range(1,len(str)) :
            if str[i-1]=='a' and str[i]=='b' :
                b +=1
            elif str[i-1]=='b' and str[i]=='a' :
                a +=1
        return min(a,b) + 1
