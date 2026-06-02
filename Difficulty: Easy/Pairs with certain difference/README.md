<h2><a href="https://www.geeksforgeeks.org/problems/pairs-with-specific-difference1533/1">Pairs with certain difference</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given an array of integers and a number k, the task is the find maximum pair sum with the following conditions on the pairs.</span></p>
<ul>
<li><span style="font-size: 18px;">Pair difference should be less than k.</span></li>
<li><span style="font-size: 18px;">Pairs should be disjoint. For example if (x, y) is a result pair, then neither x nor y should appear in any other result pair.</span></li>
<li><span style="font-size: 18px;">Sum of p pairs means sum of 2p elements in the result.</span></li>
</ul>
<p><span style="font-size: 18px;">If no valid pairs can be formed, return 0.</span></p>
<p><strong><span style="font-size: 18px;">Examples:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [3, 5, 10, 15, 17, 12, 9], K = 4
<strong>Output: </strong>62
<strong>Explanation :</strong>
The valid disjoint pairs with difference less than K are:
(3, 5), (10, 12), (15, 17)
The maximum sum obtained from these pairs is:
3 + 5 + 10 + 12 + 15 + 17 = 62
An alternative pairing could be:
(3, 5), (9, 12), (15, 17)
However, this combination results in a smaller total sum, so it is not optimal.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [5, 15, 10, 300], k = 12
<strong>Output: </strong>25<br></span><span style="font-size: 14pt;"><strong>Explanation:</strong> <br>The valid disjoint pairs with difference less than k are:
(5, 10)
The maximum sum obtained from these pairs is:
5 + 10 = 15
An alternative pairing could be:
(10, 15)
However, this combination results in a larger total sum:
10 + 15 = 25. So this pairing is optimal.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ arr.size() ≤ 10<sup>5</sup><br>0 ≤ k ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>4</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Dynamic Programming</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;