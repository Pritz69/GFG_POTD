from collections import defaultdict
class Solution:
	def countPairs(self, mat1, mat2, x):
		# code here
		count = 0
        hm1 = defaultdict(int)
        hm2 = defaultdict(int)
        n = len(mat1)
        for i in range(n):
            for j in range(n):
                a, b = mat1[i][j], mat2[i][j]
                if a + b == x:
                    count += 1
                if x - a in hm2:
                    count += hm2[x - a]
                if x - b in hm1:
                    count += hm1[x - b]
                hm1[a] += 1
                hm2[b] += 1
        return count