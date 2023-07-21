/*node class of the linked list

class Node
{
    int data;
    Node next;
    Node(int key)
    {
        data = key;
        next = null;
    }
}

*/

class Solution
{
    public static Node reverse(Node head, int k)
    {
        //Your code here
        Node curr=head;
        Node prev=null;
        Node next=null;
        int cnt =0;
        while (curr != null && cnt<k)
        {
            next=curr.next;
            curr.next=prev;
            prev=curr;
            curr=next;
            cnt +=1;
        }
        if (next != null )
        {
            Node newhead= reverse(next,k);
            head.next=newhead;
        }
        return prev;
    }
}
