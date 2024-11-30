#User function Template for python3
from collections import Counter

class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        c=Counter(s1)
        d=Counter(s2)
        for x in c :
            if x not in d :
                return False
            if c[x] != d[x] :
                return False
        for x in d :
            if x not in c :
                return False
            if c[x] != d[x] :
                return False
        return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends