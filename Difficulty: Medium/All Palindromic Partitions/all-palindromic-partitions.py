class Solution:
    def palinParts (self, s):
        # code here

        def ispali(i,j) :
            while i <= j :
                if s[i] != s[j] :
                    return False
                i +=1
                j -=1
            return True
        
        
        def func(ind,l) :
            if ind==n :
                ans.append(l.copy())
                return
            
            for j in range(ind,n) :
                if ispali(ind,j) :
                    l.append(s[ind:j+1])
                    func(j+1,l)
                    l.pop()
            
        n=len(s)
        ans=[]
        func(0,[])
        return ans