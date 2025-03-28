class Solution:
    def activitySelection(self, start, finish):
        #code here
        act=sorted(zip(start,finish),key=lambda x:x[1])
        #print(act)
        count=0
        last_time=0
        for s,f in act:
            if s>last_time:
                count+=1
                last_time=f
        return count 


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        # Read the start times
        start = list(map(int, input().strip().split()))

        # Read the finish times
        finish = list(map(int, input().strip().split()))

        # Create solution object and call activitySelection
        obj = Solution()
        print(obj.activitySelection(start, finish))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends