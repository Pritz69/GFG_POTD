class Solution:
    def matchGame(self, N):
         # code here
         if N<=4 :
             return N
         else :
             if N%5==0 :
                 return -1
             else :
                 return N%5
