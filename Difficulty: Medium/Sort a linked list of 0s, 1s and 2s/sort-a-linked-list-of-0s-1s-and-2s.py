'''
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}'''
	
class Solution:
    def segregate(self, head):
        #code here
        c0,c1,c2=0,0,0
        c=head
        while c :
            if c.data==0:
                c0 +=1
            elif c.data==1 :
                c1 +=1
            else :
                c2 +=1
            c=c.next
        ans=Node(-1)
        new=ans
        while c0 :
            n=Node(0)
            ans.next=n
            ans=ans.next
            c0 -=1
        while c1 :
            n=Node(1)
            ans.next=n
            ans=ans.next
            c1 -=1
        while c2 :
            n=Node(2)
            ans.next=n
            ans=ans.next
            c2 -=1
        
        return new.next
#{ 
 # Driver Code Starts
# Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next

        printList(Solution().segregate(head))
        print("~")

# } Driver Code Ends