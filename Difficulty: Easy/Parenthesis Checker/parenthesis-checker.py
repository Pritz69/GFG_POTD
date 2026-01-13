class Solution:
    def isBalanced(self, s):
        # code here
        if len(s)==1 :
            return False
        
        stack=[]
        
        for x in s :
            if x==")" :
                if stack and stack[-1]=="(" :
                    stack.pop()
                else :
                    stack.append(x)
            elif x=="}" :
                if stack and stack[-1]=="{" :
                    stack.pop()
                else :
                    stack.append(x)
            elif x=="]" :
                if stack and stack[-1]=="[" :
                    stack.pop()
                else :
                    stack.append(x)
            else :
                stack.append(x)
        
        if stack==[] :
            return True
        else :
            return False