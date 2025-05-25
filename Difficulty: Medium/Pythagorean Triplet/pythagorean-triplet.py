class Solution:
	def pythagoreanTriplet(self, arr):
    	# code here
    	squared_set = set(x * x for x in arr)
        
        # Check for Pythagorean triplet
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                # Calculate the square of the hypotenuse
                sum_of_squares = arr[i] * arr[i] + arr[j] * arr[j]
                
                # Check if the square root of sum_of_squares is in squared_set
                if sum_of_squares in squared_set:
                    return True
        
        return False