class Solution:
    def stringMirror(self, str : str) -> str:
        # code here
        ans=str[0]
        for i in range(1,len(str)) :
            if str[i] < str[i-1] or (i>1 and str[i]==str[i-1]):
                ans += str[i]
            else :
                break
        ans += ans[::-1]
        return ans
        

