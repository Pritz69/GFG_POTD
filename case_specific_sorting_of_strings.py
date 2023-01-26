class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        #code here
        l=[]
        u=[]
        s=list(s)
        for i in s :
            if i.islower():
                l.append(i)
            else :
                u.append(i)
        l.sort()
        u.sort()
        i=0
        j=0
        for x in range(len(s)) :
            if s[x].islower() :
                s[x]=l[i]
                i +=1
            else :
                s[x]=u[j]
                j +=1
        return ''.join(s)
