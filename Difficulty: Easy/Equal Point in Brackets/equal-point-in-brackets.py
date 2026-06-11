class Solution:
    def findIndex(self, s):
        # code here 
        tc=0
        for x in s :
            if x==')' :
                tc +=1
        o=0
        c=0
        for i,x in enumerate(s) :
            if o==(tc-c) :
                return i
            if x=='(' :
                o +=1
            elif x==')' :
                c +=1
        if o==len(s) or tc==len(s) :
            return len(s)