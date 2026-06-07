class Solution:
    def profession(self, level, pos):
        # code here
        b=bin(pos-1)[2:]
        c=0
        for x in b :
            if x=='1' :
                c +=1
        if c%2==0 :
            return "Engineer"
        else :
            return "Doctor"