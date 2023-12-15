<h2><a href="https://www.geeksforgeeks.org/problems/reach-the-nth-point5433/1">Reach the Nth point</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">There are<strong> N </strong>points on the road, you can step ahead by 1 or 2 . If you start from a point 0, and can only move from point <strong>i</strong> to point <strong>i+1</strong> after taking a step of length one, find the number of ways you can reach at point <strong>N.</strong>&nbsp;</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: <br></strong>N =<strong> </strong>4
<strong>Output: <br></strong>5
<strong>Explanation:</strong>&nbsp;Three ways to reach at 4th
point. They are {1, 1, 1, 1}, {1, 1, 2},
{1, 2, 1} {2, 1, 1}, {2, 2}.
</span>
</pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>N = 5
<strong>Output: </strong>8
<strong>Explanation: </strong>Three ways to reach at 5th
point. They are {1, 1, 1, 1, 1},
{1, 1, 1, 2}, {1, 1, 2, 1}, {1, 2, 1, 1},
{2, 1, 1, 1}{1, 2, 2}, {2, 1, 2}, {2, 2, 1}</span>
</pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You don't need to read or print anyhting. Your task is to complete the function&nbsp;<strong>nthPoint()</strong>&nbsp;which takes <strong>N</strong> as input parameter and returns the total number of ways <strong>modulo 10<sup>9</sup>&nbsp;+ 7 </strong>to reach at <strong>N<sup>th</sup> </strong>point.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:&nbsp;</strong>O(N)<br><strong>Expected Space Complexity:&nbsp;</strong>O(N)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ N ≤ 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Morgan Stanley</code>&nbsp;<code>Amazon</code>&nbsp;<code>Intel</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Dynamic Programming</code>&nbsp;<code>Algorithms</code>&nbsp;