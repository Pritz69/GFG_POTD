//{ Driver Code Starts
// Initial Template for Java
import java.io.*;
import java.util.*;

class Node {
    Node next;
    int val;

    public Node(int data) {
        val = data;
        next = null;
    }
}

class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        int t;
        t = Integer.parseInt(in.readLine());
        while (t-- > 0) {

            Node head, tail;
            String s[] = in.readLine().trim().split(" ");
            int num = Integer.parseInt(s[0]);
            head = new Node(num);
            tail = head;
            for (int i = 1; i < s.length; i++) {
                num = Integer.parseInt(s[i]);
                tail.next = new Node(num);
                tail = tail.next;
            }
            Solution ob = new Solution();
            Node temp = ob.primeList(head);
            while (temp != null) {
                out.print(temp.val + " ");
                temp = temp.next;
            }
            out.println();
            out.println("~");
        }
        out.close();
    }
}
// } Driver Code Ends


// User function Template for Java
/*
class Node{
    Node next;
    int val;
    public Node(int data){
        val=data;
        next=null;
    }
}
*/

class Solution {
    private int MAX = (int)1e5+1;
    private boolean[] prime = new boolean[MAX];
    
    void fillPrimeArray() {
        Arrays.fill(prime, true);
        prime[0] = false;
        prime[1] = false;
        
        for (int p=2; p*p < MAX; p++) {
            if (prime[p]) {
                for (int i=p*p; i < MAX; i+=p) prime[i] = false;
            }
        }}
    
    int getNearestPrime(int num) {
        if(prime[num]) return num;
        int left = num-1, right = num+1;
        
        while(left >= 0 && !prime[left]) { left--; }
        while(right < MAX && !prime[right]) { right++; }
        
        if(left < 0) return right;
        if(right > MAX-1) return left;
        
        return num-left <= right-num ? left : right;
    }
    
    Node primeList(Node head) {
        if(!prime[2]) fillPrimeArray();
        
        Node temp = head;
        
        while(temp != null) {
            temp.val = getNearestPrime(temp.val);
            temp = temp.next;
        }
        return head;
    }}

