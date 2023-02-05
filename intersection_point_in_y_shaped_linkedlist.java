class Intersect
{
    //Function to find intersection point in Y shaped Linked Lists.
	int intersectPoint(Node head1, Node head2)
	{
         // code here
         HashMap<Node,Integer> map=new HashMap<>();

         Node temp=head1;

         while(temp!=null){

             map.put(temp,temp.data);

             temp=temp.next;

         }

         Node temp1=head2;

         while(temp1!=null){

             if(map.containsKey(temp1)){

                 return map.get(temp1);

             }

             temp1=temp1.next;

         }

         return -1;
	}
}
