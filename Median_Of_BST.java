

//User function Template for Java

class Tree
{
    private static int count(Node root) 
    {
        if (root == null)
            return 0;
        return count(root.left) + count(root.right) + 1;
    }

    // Function to find the median of the binary search tree
    private static void median(Node root, int n, int[] pos, float[] m) {
        if (root != null) 
        {
            median(root.left, n, pos, m);
            pos[0]++;
            if (n % 2 == 0) 
            {
                if (pos[0] == n / 2)
                    m[0] += (root.data / 2.0);
                if (pos[0] == (n / 2 + 1))
                    m[0] += (root.data / 2.0);
            } 
            else 
            {
                if (pos[0] == (n + 1) / 2)
                    m[0] = root.data;
            }
            median(root.right, n, pos, m);
        }
    }

    // Function to find the median of the binary search tree
    public static float findMedian(Node root) {
        int c = count(root.left) + count(root.right) + 1;
        float[] m = new float[1];
        int[] pos = new int[1];
        median(root, c, pos, m);
        return m[0];
    }
}
