class Solution {
    public static Node treeFromString(String s) {
        // code here
        StringBuilder str = new StringBuilder();
        int i = 0;
        int n = s.length();
        
        while (i < n && Character.isDigit(s.charAt(i))) {
            str.append(s.charAt(i));
            i++;
        }
        
        Node root = new Node(Integer.parseInt(str.toString()));
        
        Stack<Node> stack = new Stack<>();
        stack.push(root);
        
        while (i < n) {
            switch (s.charAt(i)) {
                case '(':
                    i++;
                    break;
                case ')':
                    i++;
                    stack.pop();
                    break;
                default:
                    str = new StringBuilder();
                    
                    while (i < n && Character.isDigit(s.charAt(i))) {
                        str.append(s.charAt(i));
                        i++;
                    }
                    
                    Node node = stack.peek();
                    Node temp = new Node(Integer.parseInt(str.toString()));
                    
                    if (node.left != null) {
                        node.right = temp;
                    } else {
                        node.left = temp;
                    }
                    
                    stack.push(temp);
            }
        }
        
        return root;
    }
}
