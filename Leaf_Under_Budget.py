#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def getCount(self,root,n):
        #code here
        if not root :
            return 0
        l=[]
        q=deque()
        q.append(root)
        lvl=0
        while (q) :
            no=len(q)
            lvl +=1
            for i in range(no) :
                x=q.popleft()
                if not x.left and not x.right :
                    l.append(lvl)
                if x.left :
                    q.append(x.left)
                if x.right :
                    q.append(x.right)
        c=0
        s=0
        l.sort()
        for x in l :
            s +=x
            if s<=n :
                c +=1
            else :
                break
        return c
