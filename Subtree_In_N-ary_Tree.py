'''
class Node:
	def __init__(self, key, children=None):
		self.key = key
		self.children = children or []
	
	def __str__(self):
		return str(self.key)
'''

class Solution:
    def __init__(self):
        self.map = {}

    def duplicateSubtreeNaryTree(self, root: 'Node') -> int:
        ans = 0
        self.solve(root)

        for e in self.map:
            if self.map[e] > 1:
                ans += 1

        return ans

    def solve(self, root: 'Node') -> str:
        s = str(root.key)
        for nei in root.children:
            s += self.solve(nei)

        self.map[s] = self.map.get(s, 0) + 1
        return s
