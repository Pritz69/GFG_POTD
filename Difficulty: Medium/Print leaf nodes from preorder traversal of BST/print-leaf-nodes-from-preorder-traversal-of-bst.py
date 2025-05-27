class Solution:
    def leafNodes(self, preorder):
        stack = []
        leaf_nodes = []

        for i in range(len(preorder) - 1):
            current = preorder[i]
            next_val = preorder[i + 1]

            # Check for potential leaf
            if next_val > current:
                # We're going to the right — pop until current < next
                count = 0
                while stack and next_val > stack[-1]:
                    last = stack.pop()
                    count += 1
                if count > 0:
                    leaf_nodes.append(current)
            else:
                # If next is less than current, it's going to left
                # So current will become a parent — not a leaf
                stack.append(current)

        # Last node is always a leaf
        leaf_nodes.append(preorder[-1])

        return leaf_nodes
