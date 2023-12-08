<h2><a href="https://www.geeksforgeeks.org/problems/transform-to-prime4635/1">Transform to prime</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array of <strong>n</strong> integers. Find the <strong>minimum</strong> positive number to be inserted in array, so that sum of all elements of array becomes <strong>prime</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
N=5
arr = {2, 4, 6, 8, 12}
<strong>Output:</strong>  <br>5
<strong>Explanation</strong>: 
The sum of the array is 32 ,we can add 5 to this to make it 37 which is a prime number.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>N=3
arr = {1, 5, 7}
<strong>Output:</strong>  <br>0 
<strong>Explanation:</strong> 
The sum of the array is 13 which is already prime. </span>
</pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You don't need to read input or print anything.&nbsp;Your task is&nbsp;to complete the function <strong>minNumber()</strong> that takes array<strong> arr&nbsp;</strong>and<strong> </strong>integer<strong> N</strong> as input&nbsp;parameters and returns the minimum positive number to be inserted in the array so as to make it's sum a prime number.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(N log(log N))<br><strong>Expected Auxiliary Space:</strong> O(1).</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ N ≤ 10<sup>5</sup><br>1&nbsp;</span><span style="font-size: 18px;">≤ sum of all elements </span><span style="font-size: 18px;">≤ 10<sup>6</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Prime Number</code>&nbsp;<code>sieve</code>&nbsp;<code>Data Structures</code>&nbsp;