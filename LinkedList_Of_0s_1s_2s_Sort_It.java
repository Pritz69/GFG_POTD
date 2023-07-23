class Solution
{
    //Function to sort a linked list of 0s, 1s and 2s.
    static Node segregate(Node head)
    {
        // add your code here
        int n0=0;
        int n1=0;
        int n2=0;
        Node cur=head;
        while (cur !=null)
        {
            if (cur.data==0)
            {
                n0 +=1;
            }
            if (cur.data==1)
            {
                n1 +=1;
            }
            if (cur.data==2)
            {
                n2 +=1;
            }
            cur=cur.next;
        }
        Node curr=head;
        while(n0 !=0)
        {
            curr.data=0;
            curr=curr.next;
            n0 -=1;
        }
        while(n1 !=0)
        {
            curr.data=1;
            curr=curr.next;
            n1 -=1;
        }
        while(n2 !=0)
        {
            curr.data=2;
            curr=curr.next;
            n2 -=1;
        }
        return head;
    }
}
