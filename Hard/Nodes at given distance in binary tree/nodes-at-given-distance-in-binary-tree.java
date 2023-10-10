//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class Node  
{ 
    int data; 
    Node left, right; 
   
    public Node(int d)  
    { 
        data = d; 
        left = right = null; 
    } 
}

class GFG
{
    static Node buildTree(String str)
    {
        // Corner Case
        if(str.length() == 0 || str.equals('N'))
            return null;
        String[] s = str.split(" ");
        
        Node root = new Node(Integer.parseInt(s[0]));
        Queue <Node> q = new LinkedList<Node>();
        q.add(root);
        
        // Starting from the second element
        int i = 1;
        while(!q.isEmpty() && i < s.length)
        {
              // Get and remove the front of the queue
              Node currNode = q.remove();
        
              // Get the current node's value from the string
              String currVal = s[i];
        
              // If the left child is not null
              if(!currVal.equals("N")) 
              {
        
                  // Create the left child for the current node
                  currNode.left = new Node(Integer.parseInt(currVal));
        
                  // Push it to the queue
                  q.add(currNode.left);
              }
        
              // For the right child
              i++;
              if(i >= s.length)
                  break;
              currVal = s[i];
        
              // If the right child is not null
              if(!currVal.equals("N")) 
              {
        
                  // Create the right child for the current node
                  currNode.right = new Node(Integer.parseInt(currVal));
        
                  // Push it to the queue
                  q.add(currNode.right);
              }
              
              i++;
        }
    
        return root;
    }
    
    public static void main(String args[]) throws IOException
    {
    
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        while(t>0)
        {
            String s = br.readLine().trim();
            Node root = buildTree(s);
            Solution T = new Solution();
            int target = Integer.parseInt(br.readLine().trim());
            int k = Integer.parseInt(br.readLine().trim());
            ArrayList<Integer> res = new ArrayList<Integer>();
            res = T.KDistanceNodes(root,target,k);
            for(int i = 0;i<res.size();i++)
                System.out.print(res.get(i) + " ");
            System.out.println();    
            t--;
        }
    }
}

// } Driver Code Ends


//User function Template for Java

// class Node  
// { 
//     int data; 
//     Node left, right;
// }

class Solution
{
    static Node tar;
    public static ArrayList<Integer> KDistanceNodes(Node root, int target , int k)
    {
        Map<Node,Node>hsparent=new HashMap<>();
        parentsmark(root,hsparent);
        Map<Node,Boolean>vis=new HashMap<>();
        Queue<Node>q1=new LinkedList<>();
        getTarget(root,target);
        q1.add(tar);
        vis.put(tar,true);
        int cl=0;
        while(!q1.isEmpty()){
            int size=q1.size();
            if(cl==k)break;
            cl++;
            for(int i=0;i<size;i++){
                Node temp=q1.poll();
                if(temp.left!=null && vis.get(temp.left)==null){
                    q1.offer(temp.left);
                    vis.put(temp.left,true);
                }
                if(temp.right!=null && vis.get(temp.right)==null){
                    q1.offer(temp.right);
                    vis.put(temp.right,true);
                }
                if(hsparent.get(temp)!=null && vis.get(hsparent.get(temp))==null){
                    q1.offer(hsparent.get(temp));
                    vis.put(hsparent.get(temp),true);
                }
            }
        }
        ArrayList<Integer>ans=new ArrayList<>();
        while(!q1.isEmpty()){
            Node temp=q1.poll();
            ans.add(temp.data);
        }
        Collections.sort(ans);
        return ans;
        
        
    }
    public static void getTarget(Node node,int t){
        if(node==null)return;
        if(node.data==t){
            tar=node;
            return;
        }
        getTarget(node.left,t);
        getTarget(node.right,t);
    }
    public static void parentsmark(Node root,Map<Node,Node>hs){
        Queue<Node>q=new LinkedList<>();
        q.add(root);
        while(!q.isEmpty()){
            Node temp=q.poll();
            if(temp.left!=null){
                hs.put(temp.left,temp);
                q.add(temp.left);
            }
            if(temp.right!=null){
                hs.put(temp.right,temp);
                q.add(temp.right);
            }
        }
    }
}