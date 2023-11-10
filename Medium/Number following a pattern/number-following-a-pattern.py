#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
        ans=[]
        st=[]
        n=1
        for x in S :
            st.append(str(n))
            n +=1
            if x=='I' :
                ans += st[::-1]
                st=[]
        st.append(str(n))
        ans += st[::-1]
        return ''.join(ans)
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends