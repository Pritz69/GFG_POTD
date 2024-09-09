class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        z,o,t=0,0,0
        for x in arr :
            if x==0:
                z+=1
            elif x==1 :
                o+=1
            else :
                t +=1
        i=0
        while z :
            arr[i]=0
            i +=1
            z -=1
        while o :
            arr[i]=1
            i +=1
            o -=1
        while t :
            arr[i]=2
            i +=1
            t -=1
        return arr
#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array


if __name__ == "__main__":
    main()

# } Driver Code Ends