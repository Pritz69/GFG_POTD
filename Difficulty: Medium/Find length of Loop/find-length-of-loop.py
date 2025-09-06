'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        s,f=head,head
        while f and f.next :
            s=s.next
            f=f.next.next
            if s==f :
                c=1
                l=f.next 
                while l != s :
                    c=c+1
                    l=l.next
                    
                return c

        return 0        
        
        
        
        