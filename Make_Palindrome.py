from typing import List
class Solution:
    def makePalindrome(self, n : int, arr : List[str]) -> bool:
        # code here
        mp = {}
        for it in arr:
            rev = it[::-1]
            if rev in mp:
                mp[rev] -= 1
                if mp[rev] == 0:
                    del mp[rev]
            else:
                mp[it] = mp.get(it, 0) + 1
        if len(mp) == 0:
            return True
        if len(mp) == 1:
            curr = list(mp.keys())[0]
            rev = curr[::-1]
            return rev == curr
        return False
        
