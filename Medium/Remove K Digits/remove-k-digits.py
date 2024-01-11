#User function Template for python3

class Solution:

    def removeKdigits(self, S, K):
        # code here
        st=[]
        for x in S :
            while K >0 and st and st[-1] > x :
                st.pop()
                K -=1
            st.append(x)
        while K > 0 :
            st.pop()
            K -=1
        ans= "".join(st).lstrip('0') 
        return ans if ans else "0"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends