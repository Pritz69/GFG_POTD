#User function Template for python3

from collections import deque

class Solution:
    def __init__(self):
        self.parent_map = {}  # A dictionary to keep track of parent nodes
        self.target_node = None  # The target node we are searching for
        self.min_time = 0  # The minimum time to reach the target node

    def buildParentMap(self, node, target):
        """
        Build a parent map while searching for the target node.
        """
        if node.data == target:
            self.target_node = node
        if node.left:
            self.parent_map[node.left] = node
            self.buildParentMap(node.left, target)
        if node.right:
            self.parent_map[node.right] = node
            self.buildParentMap(node.right, target)

    def minTime(self, root, target):
        """
        Calculate the minimum time to reach the target node from the root.
        """
        self.buildParentMap(root, target)

        queue = deque()
        queue.append((self.target_node, 0))
        visited = set()

        while queue:
            current_node, time = queue.popleft()
            visited.add(current_node)

            if current_node in self.parent_map and self.parent_map[current_node] not in visited:
                queue.append((self.parent_map[current_node], time + 1))
            if current_node.left and current_node.left not in visited:
                queue.append((current_node.left, time + 1))
            if current_node.right and current_node.right not in visited:
                queue.append((current_node.right, time + 1))

            self.min_time = time  # Update the minimum time

        return self.min_time


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends