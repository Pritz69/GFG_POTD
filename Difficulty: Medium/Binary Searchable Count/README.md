<h2><a href="https://www.geeksforgeeks.org/problems/binary-searchable-elements/1">Binary Searchable Count</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given an array <strong>arr[]</strong> consisting of <strong>n</strong> distinct integers, find the maximum count of integers that are binary searchable in the given array. Binary searchable elements are determined using the standard Binary Search implementation described below.<br></span></p>
<ul>
<li><span style="font-size: 18px;">Initially l is 0 and r is size of array - 1&nbsp;</span></li>
<li><span style="font-size: 18px;">while(l &lt;= r), compute mid as floor of (l + r)/2 and compare with mid.</span></li>
<li><span style="font-size: 18px;">If the target element is same as mid, return true. Else if mid is smaller, change l = mid + 1, else change r = mid - 1.</span></li>
</ul>
<p><span style="font-size: 18px;">For example:</span></p>
<ul>
<li><span style="font-size: 18px;">In arr[] = [2, 1, 3, 4, 6, 5], the element 5 is not binary searchable. During Binary Search, the search eventually reaches the subarray containing 6, and since 6 &gt; 5, the search moves left (r = mid - 1), causing the element 5 to be skipped.</span></li>
<li><span style="font-size: 18px;">In arr[] = [2, 1, 3, 4, 5, 6], the element 5 is binary searchable because the standard Binary Search process eventually reaches and finds 5.</span></li>
</ul>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> arr[] = [1, 3, 2]<br><strong>Output:</strong> 2<br><strong>Explanation:</strong> </span><span style="font-size: 18px;">arr[0], arr[1] can be found.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input:</strong> arr[] = [2, 1, 3, 5, 4, 6]<br><strong>Output:</strong> 4<br><strong>Explanation:</strong> arr[0], a</span><span style="font-size: 18px;">rr[2], arr[4], arr[5] can be found.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ n ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Microsoft</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Greedy</code>&nbsp;<code>Algorithms</code>&nbsp;