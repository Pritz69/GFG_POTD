#User function Template for python3

def fun(ans,index,ele):
    if len(ele) == index:
        ans.add(''.join(ele))
        return
    
    for i in range(index,len(ele)):
        ele[i], ele[index] = ele[index], ele[i]
        fun(ans,index+1,ele)
        ele[i], ele[index] = ele[index], ele[i]
class Solution:
    def findPermutation(self, s):
        # Code here
        ele = [i for i in s]
        ans = set()
        fun(ans,0,ele)
        return list(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends