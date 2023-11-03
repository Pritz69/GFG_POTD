class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, n, P):
        # code here
        # Step 1: Identify and ignore elements greater than N
        for i in range(n):
            if arr[i] > n:
                arr[i] = 0
       
        # Step 2: Encode frequency information into array elements
        for i in range(n):
            if arr[i] % (n + 1) > 0:
                arr[(arr[i] % (n + 1)) - 1] += (n + 1)
       
        # Step 3: Decode the frequency information
        for i in range(n):
            arr[i] //= (n + 1)
