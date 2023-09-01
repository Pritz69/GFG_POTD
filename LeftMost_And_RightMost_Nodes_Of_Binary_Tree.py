#User function Template for python3

#User function Template for python3

'''
class Node:
    def _init_(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

def printCorner(root):
    
    # print corner data, no need to print new line
    # code here
    if not root :
        return 
    q=deque()
    q.append(root)
    while(q) :
        n=len(q)
        for i in range(n) :
            x=q.popleft()
            if i==0 or i==n-1 :
                print(x.data,end=" ")
            if x.left :
                q.append(x.left)
            if x.right :
                q.append(x.right)




