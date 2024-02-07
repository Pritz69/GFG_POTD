<h2><a href="https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article">Lowest Common Ancestor in a Binary Tree</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;"><span style="font-family: arial,helvetica,sans-serif;">Given a Binary Tree with all <strong>unique</strong> values and two nodes value,&nbsp;<strong>n1</strong> and <strong>n2</strong>. The task is to find the<strong>&nbsp;lowest common ancestor</strong> of the given two nodes. We may assume that either both n1 and n2 are present in the tree or none of them are&nbsp;present. </span></span></p>
<p><span style="font-size: 18px;">LCA: It is the first common ancestor of both the nodes n1 and n2 from bottom of tree.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>n1 = 2 , n2 = 3  
&nbsp;      1 
&nbsp;     / \ 
&nbsp;    2   3
<strong>Output: </strong><span style="font-family: arial,helvetica,sans-serif;">1
</span><strong>Explanation:
</strong></span><span style="font-size: 18px;">LCA of 2 and 3 is 1.</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>n1 = 3 , n2 = 4
           5    
      &nbsp;   /    
      &nbsp;  2  
      &nbsp; / \  
      &nbsp;3   4
<strong>Output: </strong><span style="font-family: arial,helvetica,sans-serif;">2
</span><strong>Explanation:
</strong>LCA of 3 and 4 is 2.<strong> <br></strong></span></pre>
<p style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; font-size: medium; white-space: normal;"><span style="font-size: 18px;"><strong>Example 3:</strong></span></p>
<pre><span><strong>Input:
</strong>n1 = 5 , n2 = 4
           5    
      &nbsp;   /    
      &nbsp;  2  
      &nbsp; / \  
      &nbsp;3   4
<strong>Output: </strong><span style="font-family: arial,helvetica,sans-serif;">5
</span><strong>Explanation:
</strong>LCA of 5 and 4 is 5.<strong> </strong></span></pre>
<p><span style="font-size: 18px;"><span style="font-family: arial,helvetica,sans-serif;"><strong>Your Task:</strong><br>You don't have to read, input, or print anything. Your task is to complete the function <strong>lca()&nbsp;</strong>that takes nodes, <strong>n1, and n2</strong> as parameters and returns the&nbsp;<strong>LCA </strong>node as output.&nbsp;</span></span></p>
<p><span style="font-size: 18px;"><span style="font-family: arial,helvetica,sans-serif;"><strong>Expected Time Complexity:</strong>O(N).<br><strong>Expected Auxiliary Space:</strong>O(Height of Tree).</span></span></p>
<p><span style="font-size: 18px;"><span style="font-family: arial,helvetica,sans-serif;"><strong>Constraints:</strong><br>1 ≤ Number of nodes ≤ 10<sup>5</sup><br>1 ≤ Data of a node ≤ 10<sup>5</sup></span></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Flipkart</code>&nbsp;<code>Accolite</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>OYO Rooms</code>&nbsp;<code>Snapdeal</code>&nbsp;<code>MakeMyTrip</code>&nbsp;<code>Payu</code>&nbsp;<code>Google</code>&nbsp;<code>Times Internet</code>&nbsp;<code>Cisco</code>&nbsp;<code>PayPal</code>&nbsp;<code>Expedia</code>&nbsp;<code>Twitter</code>&nbsp;<code>American Express</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;