<h2><a href="https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1">Indexes of Subarray Sum</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given an array <strong>arr[]</strong> containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value <strong><code>target</code></strong>. You need to return the <strong>1-based indices</strong> of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.</span></p>
<p><span style="font-size: 14pt;">Note: If no such array is possible then, return [-1].</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [1, 2, 3, 7, 5], target = 12
<strong>Output: </strong>[2, 4]<strong>
Explanation: </strong>The sum of elements from 2nd to 4th position is 12.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
<strong>Output: </strong>[1, 5]<strong>
Explanation: </strong>The sum of elements from 1st to 5th position is 15.
</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [5, 3, 4], target = 2
<strong>Output: </strong>[-1]<strong>
Explanation: </strong>There is no subarray with sum 2.</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:<br></strong>1 &lt;= arr.size()&lt;= 10<sup>6<br></sup>0 &lt;= arr[i] &lt;= 10<sup>3</sup></span><br><span style="font-size: 14pt;">0 &lt;=&nbsp;</span><span style="font-size: 14pt;">target</span><span style="font-size: 14pt;"> &lt;= 10<sup>9</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>Facebook</code>&nbsp;<code>Google</code>&nbsp;<code>Visa</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Algorithms</code>&nbsp;<code>Arrays</code>&nbsp;<code>Data Structures</code>&nbsp;<code>prefix-sum</code>&nbsp;<code>Searching</code>&nbsp;<code>sliding-window</code>&nbsp;