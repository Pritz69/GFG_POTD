class Solution:
    def search(self, pattern, text):
        dt = {}
        dp = {}
        n = len(text)
        m = len(pattern)
        
        for i in range(m):
            dt[text[i]] = dt.get(text[i], 0) + 1
            dp[pattern[i]] = dp.get(pattern[i], 0) + 1
        
        ans = []
        
        for i in range((n - m) + 1):
            if dt == dp:
                match = True
                for j in range(m):
                    if pattern[j] != text[i + j]:
                        match = False
                        break
                
                if match:
                    ans.append(i + 1)  
                    
            if (i + m) < n:
                dt[text[i]] -= 1
                if dt[text[i]] == 0:
                    del dt[text[i]]
                dt[text[i + m]] = dt.get(text[i + m], 0) + 1
        
        return ans 
