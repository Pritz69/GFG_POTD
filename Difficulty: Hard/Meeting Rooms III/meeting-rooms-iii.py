#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq


# } Driver Code Ends

#User function Template for python3
class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()
        available = list(range(n))
        busy, count = [], [0] * n

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                heapq.heappush(available, heapq.heappop(busy)[1])
            
            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(busy, (end_time + end - start, room))
            
            count[room] += 1

        return count.index(max(count))


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    import sys
    input = sys.stdin.read().split()
    it = iter(input)
    t = int(next(it))
    while t > 0:
        t -= 1
        n = int(next(it))
        m = int(next(it))
        meetings = []
        for _ in range(m):
            s = int(next(it))
            e = int(next(it))
            meetings.append([s, e])
        sol = Solution()
        res = sol.mostBooked(n, meetings)
        print(res)
        print("~")
# } Driver Code Ends