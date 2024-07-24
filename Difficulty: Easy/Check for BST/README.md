<h2><a href="https://www.geeksforgeeks.org/problems/check-for-bst/1">Check for BST</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given the root of a&nbsp;binary tree. Check whether it is a BST or not.<br><strong>Note: </strong>We are considering that BSTs can not contain duplicate Nodes.</span><br><span style="font-size: 18px;">A&nbsp;<strong>BST</strong>&nbsp;is defined as follows:</span></p>
<ul>
<li>
<div><span style="font-size: 18px;">The left subtree of a node contains only nodes with keys <strong>less than</strong> the node's key.</span></div>
</li>
<li>
<div><span style="font-size: 18px;">The right subtree of a node contains only nodes with keys <strong>greater than</strong> the node's key.</span></div>
</li>
<li>
<div><span style="font-size: 18px;">Both the left and right subtrees must also be binary search trees.</span></div>
</li>
</ul>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>&nbsp; &nbsp;2
 /&nbsp; &nbsp; \
1&nbsp; &nbsp; &nbsp; 3<br>        \<br>         5
<strong>Output: </strong>true 
<strong>Explanation: </strong></span>
<span style="font-size: 18px;">The left subtree of every node contains smaller keys and right subtree of every node contains greater. Hence, the tree is a BST.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>  2
&nbsp;  \
&nbsp;   7
&nbsp;    \
&nbsp;     6
&nbsp;      \
&nbsp;       9<br></span><span style="font-size: 18px;"><strong>Output: </strong>false 
<strong>Explanation: </strong>
Since the node with value 7 has right subtree nodes with keys less than 7, this is not a BST.</span><span style="font-size: 18px;"><strong>&nbsp;</strong></span></pre>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>  &nbsp;10
 /&nbsp; &nbsp; \
5&nbsp; &nbsp; &nbsp; 20<br>      /   \<br>     9     25
<strong>Output: </strong>false
<strong>Explanation: </strong>The node is present in the right subtree of 10, but it is smaller than 10.</span></pre>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(n)&nbsp;<br><strong>Expected Auxiliary Space:</strong> O(Height of the tree)<br>where n is the number of nodes in the given tree<br></span></p>
<p><span style="font-size: 18px;"><strong>Constraints:<br></strong></span><span style="font-size: 18px;">1 ≤ Number of nodes ≤ 10<sup>5<br></sup></span><span style="font-size: 18px;">1 ≤ Data of a node ≤ 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>VMWare</code>&nbsp;<code>Flipkart</code>&nbsp;<code>Accolite</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>OYO Rooms</code>&nbsp;<code>Samsung</code>&nbsp;<code>Snapdeal</code>&nbsp;<code>FactSet</code>&nbsp;<code>Hike</code>&nbsp;<code>MakeMyTrip</code>&nbsp;<code>Ola Cabs</code>&nbsp;<code>Walmart</code>&nbsp;<code>Goldman Sachs</code>&nbsp;<code>MAQ Software</code>&nbsp;<code>Adobe</code>&nbsp;<code>Linkedin</code>&nbsp;<code>Qualcomm</code>&nbsp;<code>Boomerang Commerce</code>&nbsp;<code>GreyOrange</code>&nbsp;<code>Wooker</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Binary Search Tree</code>&nbsp;<code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;