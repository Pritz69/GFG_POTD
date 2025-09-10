class Solution:
    def largestSwap(self, s):
        #code here
        n = len(s)
        last = {int(ch): i for i, ch in enumerate(s)}
        
        s = list(s)
        
        for i in range(n):
            curr = int(s[i])
            for d in range(9, curr, -1):
                if d in last and last[d] > i:
                    # swap
                    s[i], s[last[d]] = s[last[d]], s[i]
                    return "".join(s)
        return "".join(s)      
        