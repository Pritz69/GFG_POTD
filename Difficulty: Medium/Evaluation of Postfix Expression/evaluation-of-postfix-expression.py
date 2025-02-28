#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends


class Solution:
    def evaluate(self, arr):
        # code here
        ans=0
        st=[]
        for x in arr :
            if x in "+-*/" :
                a=st.pop()
                b=st.pop()
                if x=="+" :
                    st.append(a+b)
                elif x=="-" :
                    st.append(b-a)
                elif x=="*" :
                    st.append(a*b)
                elif x=="/" :
                    st.append(int(b/a))
            else :
                st.append(int(x))
        if st :
            return st.pop()
        else :
            return ans


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = input().split()
        solution = Solution()
        print(solution.evaluate(arr))
        print("~")

# } Driver Code Ends