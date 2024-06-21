#User function Template for python3


class Solution:
    def compareFrac (self, str):
        
        # code here
        a,b=str.split(",")
        na,da=a.split("/")
        na=na.strip()
        da=da.strip()
        nb,db=b.split("/")
        nb=nb.strip()
        db=db.strip()
        if (int(na)/int(da)) > (int(nb)/int(db)):
            return na+"/"+da
        elif (int(na)/int(da)) < (int(nb)/int(db)) :
            return nb + "/" + db
        else :
            return "equal"



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends