#User function Template for python3
class Solution:
    def insertAtBottom(self,st,x):
        # code here
        st.append(0)
        p=st[0]
        for i in range(1,len(st)) :
            c=st[i]
            st[i]=p
            p=c
        st[0]=x
        return st

#{ 
 # Driver Code Starts

if __name__ == "__main__":
    for _ in range(int(input())):
        n,x = map(int,input().split())
        stack = list(map(int,input().split()))
        obj = Solution()
        ans = obj.insertAtBottom(stack,x)
        for e in ans:
            print(e,end=" ")
        print()
        
        
        
# } Driver Code Ends