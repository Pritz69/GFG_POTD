class Solution:
    def reverse(self, head : Optional['Node'], k : int) -> Optional['Node']:
        # code here
        temp = Node(-1)
        temp.next = head
        prev = None
        while(k>1):
            tempo = head.next
            head.next = prev
            prev = head
            head = tempo
            k-=1
        curr = head.next
        head.next = prev
        prev2 = None
        while(curr.next):
            tempo_ = curr.next
            curr.next = prev2
            prev2 = curr
            curr = tempo_
        curr.next = prev2
        temp.next.next = curr
        return head 
