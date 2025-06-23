import sys
sys.set_int_max_str_digits(1000000)
class Solution:
    def minSum(self, arr):
        # code here
        arr.sort()
        s1=[]
        s2=[]
        for i in range(len(arr)):
            if i%2==0:
                s1.append(str(arr[i]))
            else:
                s2.append(str(arr[i]))
        n1=int("".join(s1)) if s1 else 0
        n2=int("".join(s2)) if s2 else 0
        return str(n1+n2)