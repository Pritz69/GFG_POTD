<h2><a href="https://www.geeksforgeeks.org/problems/longest-span-with-same-sum-in-two-binary-arrays5142/1">Longest Span in two Binary Arrays</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given two<strong> </strong>binary arrays, <strong>a1[] and a2[]</strong>. Find the<strong> length </strong>of longest common span<strong> </strong>(i, j) where j&gt;= i such that a1[i] + a1[i+1] + .... + a1[j] =&nbsp; a2[i] + a2[i+1] + ... + a2[j].</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>a1[] = [0, 1, 0, 0, 0, 0], a2[] = [1, 0, 1, 0, 0, 1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest span with same sum is from index 1 to 4 following zero based indexing.</span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>a1[] = [0, 1, 0, 1, 1, 1, 1], a2[] = [1, 1, 1, 1, 1, 0, 1]
<strong>Output:</strong> 6<br><strong>Explanation:</strong> The longest span with same sum is from index 1 to 6 following zero based indexing.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= a1.size() = a2.size() &lt;= 10<sup>6</sup><br>0 &lt;= a1[i], a2[i] &lt;= 1</span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>prefix-sum</code>&nbsp;<code>sliding-window</code>&nbsp;<code>Arrays</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;