<h2><a href="https://www.geeksforgeeks.org/problems/game-of-xor1541/1">Game of XOR</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array <strong>A</strong>&nbsp;of size <strong>N.&nbsp;</strong>The value of an&nbsp;array is denoted by&nbsp;the bit-wise <strong>XOR</strong> of all elements it contains. Find the bit-wise XOR of the values of all subarrays of A. </span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: <br></strong>N <strong>= </strong>3 <br>A = [1,2,3] 
<strong>Output: <br></strong>2
<strong>Explanation:</strong>
xor[1] = 1
xor[1, 2] = 3
xor[2, 3] = 1
xor[1, 2, 3] = 0
xor[2] = 2
xor[3] = 3
Result : 1 ^ 3 ^ 1 ^ 0 ^ 2 ^ 3 = 2
</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: <br></strong>N<strong> </strong>=<strong> </strong>2<br>A = [1,2]
<strong>Output: <br></strong>0
<strong>Explanation:</strong>
xor[1] = 1
xor[1, 2] = 3
xor[2] = 2
Result : 1 ^ 3 ^ 2 = 0</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You don't need to read input or print anything. Your task is to complete the function <strong>gameOfXor()</strong> which takes an integer N and&nbsp;array A[] as input parameters and returns the answer.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(N)<br><strong>Expected Auxiliary Space:</strong> O(1)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong></span><br><span style="font-size: 18px;">1 &lt;= N &lt;= 10<sup>5</sup></span><br><span style="font-size: 18px;">0 &lt;= A[i] &lt;= 10<sup>9</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Mathematical</code>&nbsp;<code>Bit Magic</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;