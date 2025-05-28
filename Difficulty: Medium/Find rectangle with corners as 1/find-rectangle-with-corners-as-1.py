class Solution:    
    def ValidCorner(self,mat): 
        # Code here 
        n=len(mat)
        m=len(mat[0])
        for i in range(n) :
            for j in range(i+1,n) :
                cnt=0
                for k in range(m) :
                    if mat[i][k]==1 and mat[j][k]==1 :
                        cnt +=1
                if cnt >= 2 :
                    return True
        return False