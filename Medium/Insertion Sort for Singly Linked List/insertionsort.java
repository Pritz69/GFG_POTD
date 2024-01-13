

//User function Template for Java

/*class Node
    {
        int data;
        Node next;
        Node(int d) {data = d; next = null; }
    }
    */
class Solution
{
    public static Node insertionSort(Node head)
    {
        //code here
        Node curr = head;
        Node prev = null;

        while (curr != null) {
            if (prev != null && prev.data > curr.data) {
                Node temp = head;
                while (temp != curr) {
                    if (temp.data > curr.data) {
                        int val = temp.data;
                        temp.data = curr.data;
                        curr.data = val;
                    }
                    temp = temp.next;
                }
            }
            prev = curr;
            curr = curr.next;
        }

        return head;
    }
}
