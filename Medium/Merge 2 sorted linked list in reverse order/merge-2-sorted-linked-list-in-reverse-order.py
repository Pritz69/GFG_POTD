#User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

class Solution:
    def mergeResult(self, h1, h2):
        #return head of merged list
        def reversal(head) :
            prev=None
            curr=head
            while curr :
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            return prev
        if not h2 :
            return reversal(h1)
        if not h1 :
            return reversal(h2)
        head=None
        if h1.data < h2.data :
            head=h1
            h1=h1.next
        else :
            head=h2
            h2=h2.next
        temp=head
        while h1 and h2 :
            if h1.data < h2.data :
                temp.next=h1
                temp=temp.next
                h1=h1.next
            else :
                temp.next=h2
                temp=temp.next
                h2=h2.next
        if h1 :
            temp.next=h1
            temp=temp.next
            h1=h1.next
        if h2 :
            temp.next=h2
            temp=temp.next
            h2=h2.next
        return reversal(head)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1,n2=[int(x) for x in input().split()]
        
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
            
        arr2=[int(x) for x in input().split()]
        ll2=Llist()
        tail=None
        for nodeData in arr2:
            tail=ll2.insert(nodeData,tail)
        
        
        ob = Solution()
        resHead=ob.mergeResult(ll1.head,ll2.head)
        printList(resHead)
        print()
        
    
    
# } Driver Code Ends