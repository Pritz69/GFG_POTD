class Solution:
	def minJumps(self, arr):
	    # code here
	    n = len(arr)
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1

        jumps = 1
        farthest = arr[0]
        end = arr[0]

        for i in range(1, n):
            if i == n-1:
                return jumps  # reached end

            farthest = max(farthest, i + arr[i])

            if i == end:  # must jump now
                jumps += 1
                end = farthest
                if end <= i:
                    return -1  # stuck

        return -1
	            
	        
	    
	        
	        
	        
	        