class Solution:
    def evaluatePostfix(self, arr):
        # code here
        s = []
        for x in arr:
            if x.lstrip('-').isdigit():   # handles negative numbers too
                s.append(int(x))
            else:
                b = s.pop()
                a = s.pop()
                if x == "+":
                    s.append(a + b)
                elif x == "-":
                    s.append(a - b)
                elif x == "*":
                    s.append(a * b)
                elif x == "/":
                    s.append(a // b)  # FIXED: correct integer division
                elif x == "^":
                    s.append(pow(a, b))
        return s[-1] if s else 0