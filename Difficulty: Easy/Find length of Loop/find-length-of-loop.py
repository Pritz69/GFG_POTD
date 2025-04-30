#User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #Your code here
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            
            if s == f:
                cnt = 1
                node = s.next
                while node != s:
                    cnt += 1
                    node = node.next
                return cnt
        
        return 0




#{ 
 # Driver Code Starts
import sys


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(node):
    while node:
        print(node.data, end=' ')
        node = node.next
    print()


def loop_here(head, pos):
    if pos == 0:
        return

    walk = head
    for _ in range(1, pos):
        walk = walk.next

    tail = head
    while tail.next:
        tail = tail.next

    tail.next = walk


if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split('\n')
    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        k = int(data[index + 1])
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        loop_here(head, k)
        ob = Solution()
        res = ob.countNodesInLoop(head)
        print(res)
        print("~")
        index += 2

# } Driver Code Ends