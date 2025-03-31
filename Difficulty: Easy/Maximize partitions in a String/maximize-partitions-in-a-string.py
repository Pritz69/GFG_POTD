class Solution:
    def maxPartitions(self , s):
        # code here
        d={}
        for i,x in enumerate(s) :
            d[x]=i
        ans=0
        e=0
        for i in range(len(s)) :
            e=max(e,d[s[i]])
            if i==e :
                ans +=1
        return ans

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends