<h2><a href="https://www.geeksforgeeks.org/problems/node-at-distance/1">Count the nodes at distance K from leaf</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a binary tree with n nodes and a non-negative integer k, the task is to count the number of special nodes. <br>A node is considered special if there exists at least one leaf in its subtree such that the distance between the node and leaf is exactly k.<br></span></p>
<p><span style="font-size: 18px;"><strong>Note:</strong> Any such node should be counted only once. For example, if a node is at a distance k from 2 or more leaf nodes, then it would add only 1 to our count.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong><br>Binary tree
        1
&nbsp;     /   \
&nbsp;    2     3
&nbsp;  /  \   /  \
&nbsp; 4   5  6    7
&nbsp;         \ 
&nbsp;         8
k = 2
<strong>Output: <br></strong>2<strong>
Explanation: <br></strong>There are only two unique nodes that are at a distance of 2 units from the leaf node. (node 3 for leaf with value 8 and node 1 for leaves with values 4, 5 and 7) Note that node 2 isn't considered for leaf with value 8 because it isn't a direct ancestor of node 8.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:<br></strong>Binary tree<strong><br></strong></span><span style="font-size: 18px;"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1
&nbsp;        /
&nbsp;       3
&nbsp;      /
&nbsp;     5
&nbsp;   /  \
&nbsp;  7    8
         \
&nbsp;         9
k = 4
<strong>Output: <br></strong>1<strong>
Explanation: <br></strong>Only one node is there which is at a distance of 4 units from the leaf node.(node 1 for leaf with value 9) </span></pre>
<p><strong><span style="font-size: 18px;">Your Task:</span></strong><br><span style="font-size: 18px;">You don't have to read&nbsp;input or print anything. Complete the function <strong>printKDistantfromLeaf()&nbsp;</strong>that takes root<strong> node </strong>and<strong> k </strong>as inputs and <strong>returns </strong>the number of nodes that are at distance k from a leaf node.&nbsp;</span></p>
<p dir="ltr"><span style="font-size: 18px;"><strong>Expected Time Complexity: </strong>O(n).<br><strong>Expected Auxiliary Space: </strong>O(Height of the Tree).</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= n &lt;= 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Flipkart</code>&nbsp;<code>Microsoft</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;