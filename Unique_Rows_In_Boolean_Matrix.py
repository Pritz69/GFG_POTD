from typing import List


class Solution:
    def uniqueRow(self, row, col, matrix):
    #complete the function
        s=set()
        l=[]
        for r in matrix :
            if str(r) not in s :
                s.add(str(r))
                l.append(r)
        return l
