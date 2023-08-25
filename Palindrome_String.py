#User function Template for python3
class Solution:
    def isPalindrome(self, S):
        # code here
        l=0
        r=len(S)-1
        while l<=r :
            if S[l]!=S[r] :
                return 0
            l +=1
            r -=1
        return 1
