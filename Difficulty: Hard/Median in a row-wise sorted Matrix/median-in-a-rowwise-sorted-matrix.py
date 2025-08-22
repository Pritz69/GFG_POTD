class Solution:
    def median(self, mat):
    	# code here 
    	ans=[]
    	for x in mat :
    	    for y in x :
    	        ans.append(y)
    	ans.sort()
        n=len(ans)
        return ans[n//2]
    	