<h2><a href="https://www.geeksforgeeks.org/problems/is-it-a-tree/1">Check if a given graph is tree or not</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">You are given an undirected graph of <strong>N</strong> nodes and <strong>M</strong> edges. Return 1 if the graph is a tree, else return 0.</span></p>
<p><span style="font-size: 18px;"><strong>Note:</strong> The input graph can have self-loops and multiple edges.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong></span>
<span style="font-size: 18px;">N = 4, M = 3</span>
<span style="font-size: 18px;">G = [[0, 1], [1, 2], [1, 3]]</span>
<span style="font-size: 18px;"><strong>Output:</strong> <br>1</span>
<span style="font-size: 18px;"><strong>Explanation: <br></strong>Every node is reachable and the graph has no loops, so it is a tree</span>
</pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong></span><span style="font-size: 18px;">N = 4, M = 3</span>
<span style="font-size: 18px;">G = [[0, 1], [1, 2], [2, 0]]</span>
<span style="font-size: 18px;"><strong>Output:</strong> <br>0</span>
<span style="font-size: 18px;"><strong>Explanation:</strong> <br>3 is not connected to any </span><span style="font-size: 18px;">node and there is a loop 0-&gt;1-&gt;2-&gt;0, so</span> <span style="font-size: 18px;">it is not a tree.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Your Task:&nbsp;&nbsp;</strong><br>You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>isTree()</strong> which takes the integer N (the number nodes in the input graph) and the edges representing the graph as input parameters and returns 1 if the input graph is a tree, else 0.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(N+M)<br><strong>Expected Auxiliary Space:</strong> O(N)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= N &lt;= 2*10<sup>5</sup><br>0 &lt;= M &lt;= 2*10<sup>5</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>DFS</code>&nbsp;<code>Graph</code>&nbsp;<code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;