<h2><a href="https://www.geeksforgeeks.org/problems/black-and-white-1587115620/1">Non-Attacking Black and White Knights</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given two integers <strong>n</strong> and <strong>m </strong>representing the dimensions of a chessboard, find the number of ways to place one black knight and one white knight on the chessboard such that they cannot attack each other.</span></p>
<p><span style="font-size: 18px;"><strong>Note:<br></strong></span></p>
<ul>
<li><span style="font-size: 18px;">The knights have to be placed on different squares. </span></li>
<li><span style="font-size: 18px;">A knight can move two squares horizontally and one square vertically (L shaped), or two squares vertically and one square horizontally (L shaped). </span></li>
<li><span style="font-size: 18px;">The knights attack each other if one can reach the other in one move.</span></li>
</ul>
<p><strong><span style="font-size: 18px;">Examples:</span></strong></p>
<pre><strong><span style="font-size: 18px;">Input: </span></strong><span style="font-size: 18px;">n</span><span style="font-size: 18px;"> = 2, m = 2
<strong>Output: </strong>12 
<strong>Explanation</strong>: There are 12 ways we can place a black and a white Knight on this chessboard such that they cannot attack each other.</span>
</pre>
<pre><strong><span style="font-size: 18px;">Input: </span></strong><span style="font-size: 18px;">n = 2, m = 3
<strong>Output: </strong>26
<strong>Explanation</strong>: There are 26 ways we can place a black and a white Knight on this chessboard such that they cannot attack each other.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong></span><br><span style="font-size: 18px;">1 ≤ n ≤ 200<br>1 ≤ m ≤ 225</span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Backtracking</code>&nbsp;<code>Algorithms</code>&nbsp;