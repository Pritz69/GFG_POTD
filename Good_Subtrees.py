#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def goodSubtrees(self, root, k):
        #code here
        global ans
        ans = 0
        self.help(root, k)
        return ans
    
    def help(self, root, k):
        if not root:
            return set()
        l = self.help(root.left, k)
        r = self.help(root.right, k)
    
        tot = set()
        for x in l:
            tot.add(x)
    
        for x in r:
            tot.add(x)
    
        tot.add(root.data)
    
        if len(tot) <= k:
            global ans
            ans += 1
    
        return tot
