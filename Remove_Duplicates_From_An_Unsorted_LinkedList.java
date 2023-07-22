/* The structure of linked list is the following
class Node
{
    int data;
    Node next;
    Node(int d) {
        data = d; 
        next = null;
    }
}
*/

class Solution
{
    //Function to remove duplicates from unsorted linked list.
    public Node removeDuplicates(Node head) 
    {
         // Your code here
         HashSet<Integer> h=new HashSet<>();
         Node curr=head;
         Node prev=null;
         while(curr!=null)
         {
             int v=curr.data;
             if (h.contains(v))
             {
                 prev.next=curr.next;
             }
             else
             {
                 h.add(v);
                 prev=curr;
             }
             curr=curr.next;
         }
         return head;
    }
}
