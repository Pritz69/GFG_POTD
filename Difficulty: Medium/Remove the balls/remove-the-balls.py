#User function Template for python3
class Solution:
    def findLength(self, colour, radius):
        sc=[colour[0]]
        sr=[radius[0]]
        ans=0
        for i in range(1,len(colour)) :
            if sc and sr and colour[i]==sc[-1] and radius[i]==sr[-1] :
                sc.pop()
                sr.pop()
            else :
                sc.append(colour[i])
                sr.append(radius[i])
        
        return len(sc)