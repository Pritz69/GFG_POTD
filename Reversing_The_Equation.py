class Solution:
    def reverseEqn(self, s):
        # code here
        c=[]
        o=[]
        n=''
        for x in s :
            if x not in "+-/*" :
                n += x
            else :
                c.append(n)
                n =''
                o.append(x)
        c.append(n)
        ans =''
        while c :
            ans += c.pop()
            if o :
                ans += o.pop()
        return ans
