class Solution:
    def CamelCase(self,N,Dictionary,Pattern):
        ans = []
        for word in Dictionary:
            pi = 0
            for w in word:
                if w.isupper():
                    if Pattern[pi]==w:
                        pi+=1
                        if pi==len(Pattern):
                            ans.append(word)
                            break
                    else:
                        break
        return [-1] if len(ans)==0 else ans
