<h2><a href="https://www.geeksforgeeks.org/problems/power-of-2-and-subsequences0759/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article">Power Of 2 and Subsequences</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given is an array<strong> A[]</strong> of size <strong>N</strong>. Return the number of non-empty subsequences such that the product of all numbers in the subsequence is <strong>Power of 2</strong>. Since the answer may be too large, return it modulo 10<sup>9</sup> + 7.</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:</span></strong>
<span style="font-size:18px">N = 3
A[] = {1, 6, 2}</span>
<strong><span style="font-size:18px">Output:</span></strong>
<span style="font-size:18px">3</span>
<span style="font-size:18px"><strong>Explanation:</strong></span>
<span style="font-size:18px">The subsequence that </span>
<span style="font-size:18px">can be chosen is {1},</span>
<span style="font-size:18px">{2} and {1,2}.</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:</span></strong>
<span style="font-size:18px">N = 3
A[] = {3, 5, 7}</span>
<strong><span style="font-size:18px">Output:</span></strong>
<span style="font-size:18px">0</span>
<strong><span style="font-size:18px">Explanation:</span></strong>
<span style="font-size:18px">No subsequences exist.</span>
</pre>

<p><strong><span style="font-size:18px">Your Task:</span></strong></p>

<p><span style="font-size:18px">You don't need to read input or print anything. Your task is to complete the function numberOfSubsequences() which takes an integer N and an array A and returns the number of subsequences that exist. As this number can be very large return the result under modulo 10<sup>9</sup>+7.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N &lt;= 10<sup>5</sup><br>
1 &lt;= A[i] &lt;= 10<sup>9</sup></span></p>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Mathematical</code>&nbsp;<code>Bit Magic</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;