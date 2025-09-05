'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        c0,c1,c2=0,0,0
        c=head
        while c :
            if c.data==0 :
                c0 +=1
            elif c.data==1 :
                c1 +=1
            else :
                c2 +=1
            c=c.next
        c=head
        while c :
            if c0 > 0 :
                c.data=0
                c0 -=1
            elif c1 > 0 :
                c.data=1
                c1 -=1
            else :
                c.data=2
                c2 -=1
            c=c.next 
        
        return head
    