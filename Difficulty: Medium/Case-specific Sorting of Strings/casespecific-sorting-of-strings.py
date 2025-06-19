class Solution:
    def caseSort(self,s):
        #code here
        a=[]
        b=[]
        for x in s :
            if ord(x) >= 65 and ord(x) <= 90 :
                a.append(x)
            else :
                b.append(x)
        a.sort()
        b.sort()
        ans=[]
        i,j=0,0
        for x in s :
            if ord(x) >= 65 and ord(x) <= 90 :
                ans.append(a[i])
                i+=1
            else :
                ans.append(b[j])
                j+=1
        return "".join(ans)