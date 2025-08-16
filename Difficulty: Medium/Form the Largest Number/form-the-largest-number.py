from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        # Step 1: Convert to strings
        arr = list(map(str, arr))

        # Step 2: Custom comparator
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Step 3: Sort with comparator
        arr.sort(key=cmp_to_key(compare))

        # Step 4: Join result
        result = ''.join(arr)

        # Step 5: Handle case like [0, 0, 0]
        return result if result[0] != '0' else '0'
	    