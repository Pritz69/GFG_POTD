#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        d={}
        for x in arr :
            d[x]=d.get(x,0)+1
        ans=0
        for x in arr :
            if target-x in d :
                if x==target-x :
                    ans += d[target-x]-1
                else :
                    ans += d[target-x]
        return ans//2


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends