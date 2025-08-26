class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        l,r=0,0
        while r < len(s2) :
            if l == len(s1):
                return True
            c=s1[l]
            if s2[r]==c :
                l +=1
            r +=1
        return l==len(s1)
        