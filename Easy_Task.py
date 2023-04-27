from typing import List
from collections import defaultdict

class Solution:
    def easyTask(self,n,s,q,queries) -> List[int]:
        # code here
        ans=[]
        for x in queries :
            t=x[0]
            if t=='1' :
                i=int(x[1])
                r=x[2]
                s=s[:i] + r + s[i+1:]
            else :
                l=int(x[1])
                ri=int(x[2])
                k=int(x[3])
                ns=s[l:ri+1]
                freq = [0] * 26
                for c in ns:
                    freq[ord(c) - ord('a')] += 1
                count=0
                for p in range(25,-1,-1) :
                    while count<k and freq[p]>0 :
                        count +=1
                        freq[p] -=1
                    if count == k :
                        ans.append(chr(ord('a')+p))
                        break
        return ans




optimized version,still getting tle after 163 cases. The same approach in Java is getting accepted. I think this is because Python is slow.
