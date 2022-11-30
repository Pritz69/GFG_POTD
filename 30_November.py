class Solution:
    
    def reorderList(self,head):
        slow = head
        fast = head.next
        
        #finding the middle element
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #slow will be middle element we break at middle ele to have two seperate linked lists
        second = slow.next
        slow.next = None
        prev = None
        
        
        # now we reverse the second linked list
        while second:
            temp = second.next
            second.next = prev
            prev,second = second,temp
        
        #assigning starting point of first and second linked list    
        first,second = head,prev
        
        # now we merge these two linked list in the given order
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        
        return head
