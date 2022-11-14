class Solution:

    def numberOfSubsequences (self,S,W):

        # code here 

        S=list(S)

        counter=0

        for i in range(len(S)):

            k=0

            for j in range(i,len(S)):

                if S[j]== W[k]:

                    k+=1

                    S[j]="*"

                if k==len(W):

                    counter+=1

                    break

        return counter
