#User function Template for python3

class Solution:
    def kthElement(self, k, array1, array2):
        index1 = index2 = mergedIndex = currentElement = 0
        length1 = len(array1)
        length2 = len(array2)
       
        # Traverse both arrays and merge elements until we reach the k-th position
        while index1 < length1 and index2 < length2:
            if mergedIndex == k:
                return currentElement
           
            if array1[index1] < array2[index2]:
                currentElement = array1[index1]
                index1 += 1
            else:
                currentElement = array2[index2]
                index2 += 1
           
            mergedIndex += 1
       
        # If there are remaining elements in array1
        while index1 < length1:
            if mergedIndex == k:
                return currentElement
           
            currentElement = array1[index1]
            index1 += 1
            mergedIndex += 1
       
        # If there are remaining elements in array2
        while index2 < length2:
            if mergedIndex == k:
                return currentElement
           
            currentElement = array2[index2]
            index2 += 1
            mergedIndex += 1
       
        return currentElement


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(k, a, b))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends