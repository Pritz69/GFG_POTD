#User function Template for python3

class Solution:
    def pattern (self, arr):
        # code here
        def palin(a) :
            l,r=0,len(a)-1
            while l <= r :
                if a[l]==a[r] :
                    l +=1
                    r -=1
                else :
                    return False
            return True
        ans=""
        for i in range(len(arr)) :
            a=[]
            for j in range(len(arr[0])) :
                a.append(arr[i][j])
            if palin(a) :
                ans += str(i) +" "+"R"
                return ans
        for j in range(len(arr[0])) :
            a=[]
            for i in range(len(arr)) :
                a.append(arr[i][j])
            #print(a)
            if palin(a) :
                ans += str(j) + " "+"C"
                return ans
        return "-1" 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends