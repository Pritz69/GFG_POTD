<h2><a href="https://www.geeksforgeeks.org/problems/minimum-toogles-to-partition0135/1">Minimum Toggle to Partition</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given an array <strong>arr[]</strong> containing only 0 and 1. Find the minimum toggles (switch from 0 to 1 or vice-versa) required such the array become partitioned, i.e., it has first 0s then 1s.</span></p>
<p><strong><span style="font-size: 18px;">Examples:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr = [1, 0, 1, 1, 0]
<strong>Output:</strong> 2
<strong>Explaination:</strong> The changed array will be [0, 0, 1, 1, 1]. So the number of toggles here required is 2.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input:</strong> arr = [0, 1, 0, 0, 1, 1, 1]
<strong>Output:</strong> 1
<strong>Explaination:</strong> The changed array will be [0, 0, 0, 0, 1, 1, 1]. Required toggles are 1.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ arr.size() ≤ 10<sup>5</sup><br>0 ≤ arr[i] ≤ 1</span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Mathematical</code>&nbsp;<code>Algorithms</code>&nbsp;