
class Solution:
    def decodedString(self, s):
        # code here
        nums = []
        st = []
        current = []
    
        num = 0
    
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                nums.append(num)
                st.append(current)
                current = []
                num = 0
            elif c == ']':
                temp = ''.join(current)
                current = st.pop()
                count = nums.pop()
                current.append(temp * count)
            else:
                current.append(c)
    
        return ''.join(current)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends