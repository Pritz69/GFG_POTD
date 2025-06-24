class Solution:
    def maxSubseq(self, s, k):
        #code here
        stack = []
        n, cnt = len(s), 0
        for c in s:
            while stack and cnt < k and stack[-1] < c:
                stack.pop()
                cnt +=1
            stack.append(c)
        while len(stack) > n - k:
            stack.pop()
            
        return ''.join(stack)
        
     