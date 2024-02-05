//{ Driver Code Starts
import java.util.Scanner;

// Node Class
class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }
}



public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();
            Node start = null;
            Node temp=null, r = null;

            // Create linked list from the array arr[].
            // Created linked list will be 1->2->11->56->12
            if (n > 0) {
                int arr = sc.nextInt();

                temp = new Node(arr);
                start = temp;
                r = start;
            }

            for (int i = 0; i < n - 1; i++) {
                int arr = sc.nextInt();
                temp = new Node(arr);
                r.next = temp;
                r = r.next;
            }

            if (n > 0)
            {
                temp.next = start;
                r = temp; 
            }


            int x = sc.nextInt();
            Solution ob = new Solution();
            start = ob.sortedInsert(start, x);
            printList(start);
            r = start;
            while (r != start.next) {
                temp = start;
                start = start.next;
                temp = null;
            }
            temp = null;
        }
    }

    /* Function to print Nodes in a given linked list */
    static void printList(Node start) {
        Node temp;

        if (start != null) {
            temp = start;
            do {
                System.out.print(temp.data + " ");
                temp = temp.next;
            } while (temp != start);
            System.out.println();
        }
    }
}

// } Driver Code Ends


//User function Template for Java
class Solution {
    public Node sortedInsert(Node head, int data) {
        // code here
        Node curr = head;
        Node new_node = new Node(data);
        if(curr== null){
            new_node.next = new_node;
            return new_node;
        }
        else if(curr.data>=data){
            while(curr.next!=head){
                curr= curr.next;
            }
            curr.next= new_node;
            new_node.next = head;
            return new_node;
        }
        else{
            while(curr.next!=head && curr.next.data<data)
            curr=curr.next;
            new_node.next = curr.next;
            curr.next = new_node;
            return head;
        }
    }
}