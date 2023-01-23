class Solution:
    def removePair(self,s):
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        if not stack:
            return "-1"
        return ''.join(stack)
