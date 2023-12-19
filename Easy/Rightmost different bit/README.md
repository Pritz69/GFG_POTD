<h2><a href="https://www.geeksforgeeks.org/problems/rightmost-different-bit-1587115621/1">Rightmost different bit</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given two numbers <strong>M</strong> and <strong>N</strong>. The task is to find the position of the&nbsp;rightmost <strong>different</strong> bit in the binary representation of numbers.&nbsp;</span><span style="font-size: 18px;">If both M and N are the same then return -1 in this case.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:&nbsp;</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: <br></strong>M = 11, N = 9
<strong>Output:</strong> <br>2
<strong>Explanation:</strong> <br>Binary representation of the given numbers are: 1011 and 1001, 2nd bit from right is different.</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: <br></strong>M = 52, N = 4
<strong>Output</strong>: <br>5
<strong>Explanation</strong>: <br>Binary representation of the given numbers are: 110100 </span><span style="font-size: 18px;">and 0100, 5th-bit from right is different.</span>
</pre>
<p><span style="font-size: 18px;"><strong>User Task:</strong><br>The task is to complete the function <strong>posOfRightMostDiffBit</strong>() which takes<strong> </strong>two arguments <strong>M</strong> and <strong>N</strong> and returns the position of first different bits in M and N from right. If both m and n are the same then return -1 in this case.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(max(log M, log N)).<br><strong>Expected Auxiliary Space:</strong>&nbsp;O(1).</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>0 &lt;= M, N &lt;= 10<sup>9</sup><br></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Bit Magic</code>&nbsp;<code>Data Structures</code>&nbsp;