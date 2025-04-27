#User function Template for python3

class Solution:
    def multiplyStrings(self, s1, s2):
        # code here
        # return the product string
        i1 = 0
        i2 = 0
        sign = False
        for c in s1:
            if c=='-':
                sign=True
            else:
                num = ord(c)-ord('0')
                i1 = i1*10+num
        for c in s2:
            if c=='-':
                if sign:
                    sign = False
                else:
                    sign = True
            else:
                num = ord(c)-ord('0')
                i2 = i2*10+num
        i3 = i1*i2
        if i3==0:
            return '0'
        arr = ['0','1','2','3','4','5','6','7','8','9']
        ans = ""
        while i3:
            rem = i3%10
            num = arr[rem]
            ans+= num
            i3//=10
        result = ""
        if sign:
            result += '-'
        for i in range(len(ans)-1,-1,-1):
            result+=ans[i]
        
        # print(i1,i2,ans)
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a = input()
        b = input()
        print(Solution().multiplyStrings(a.strip(), b.strip()))

        print("~")

# } Driver Code Ends