
class Solution:
    def union(self, head1,head2):
        # code here
        # return head of resultant linkedlist
        s=set()
        curr1=head1
        while (curr1) :
            s.add(curr1.data)
            curr1 = curr1.next
        curr2=head2
        while (curr2) :
            s.add(curr2.data)
            curr2 = curr2.next
        l=list(s)
        l.sort()
        ans = Node(None)
        head = ans
        for x in l :
            head.next = Node(x)
            head = head.next
        return ans.next
