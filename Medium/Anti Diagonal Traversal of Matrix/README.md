<h2><a href="https://www.geeksforgeeks.org/problems/print-diagonally1623/1">Anti Diagonal Traversal of Matrix</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Give a N*N square <strong>matrix</strong>, return an array of its <strong>anti-diagonals </strong>in top-leftmost to bottom-rightmost order. In an element of a <strong>anti-diagonal (i, j)</strong>, surrounding elements will be <strong>(i+1, j-1)</strong> and <strong>(i-1, j+1)</strong>. Look at the examples for more clarity.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
N = 2
matrix[][] = 1 2<br>            3 4
<strong>Output:</strong>
1 2 3 4
<strong>Explanation:</strong>
List of anti-diagnoals in order is<br>{1}, {2, 3}, {4}</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
N = 3
matrix[][] = 3 2 3<br>            4 5 1<br>            7 8 9<br><strong>Output:</strong>
3 2 4 3 5 7 1 8 9</span></pre>
<pre><strong>Explanation:</strong>
List of anti-diagnoals in order is<br>{3}, {2, 4}, {3, 5, 7}, {1, 8}, {9}</pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You dont need to read input or print anything. Complete the function <strong>antiDiagonal</strong><strong>Pattern()</strong> that takes <strong>matrix </strong>as input parameter and returns a <strong>list of integers </strong>in order of the values visited in the anti-Diagonal&nbsp;pattern.&nbsp;</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(N * N)<br><strong>Expected Auxiliary Space:</strong> O(N * N)</span><br>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= N &lt;= 100<br>0 &lt;= mat[i][j] &lt;= 100</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Misc</code>&nbsp;<code>Matrix</code>&nbsp;<code>Data Structures</code>&nbsp;