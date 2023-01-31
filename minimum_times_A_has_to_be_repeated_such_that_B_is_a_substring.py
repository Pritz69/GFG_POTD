class Solution:
    def minRepeats(self, A, B):
        rep = A
        count = 1
        while len(rep)<len(B):

            rep+=A

            count+=1
        if B in rep:

            return count
        rep+=A
        if B in rep:

            count+=1

            return count
        return -1
