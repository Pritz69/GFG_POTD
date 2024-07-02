<h2><a href="https://www.geeksforgeeks.org/problems/find-index4752/1?page=1&difficulty%5B%5D=-2&category%5B%5D=Arrays&sortBy=">Find Index</a></h2><h3>Difficulty Level : Difficulty: School</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an unsorted array <strong>arr[]</strong> of <strong>n</strong> integers and a <strong>key</strong> which is present in this array. You need to write a program to find the <strong>start index</strong>( index where the element is first found from left in the array ) and <strong>end index</strong>( index where the element is first found from right in the array ).<strong>(0 based indexing is used)</strong><br></span><span style="font-size: 18px;">If the key does not exist in the array then return -1 for both start and end index in this case.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
n = 6
arr[] = { 1, 2, 3, 4, 5, 5 }
key = 5
<strong>Output:</strong>  {4, 5}
<strong>Explanation</strong>:
5 appears first time at index 4 and appears last time at index 5.
<strong>(0 based indexing)</strong>
</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>n = 6
arr = { 6, 5, 4, 3, 1, 2 }
key = 4
<strong>Output:</strong>  {2, 2} <br><strong style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">Explanation</strong><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">:<br></span></span><span style="font-size: 18px;">4 appears first time and last time at index 2.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You just need to complete the function <strong>findIndex()</strong> that takes<strong> </strong>array<strong> arr,</strong> integer <strong>n</strong> and integer<strong> key </strong>as parameters<strong>&nbsp;</strong>and returns an array of length 2 in which at first index contains the value of start index and at the second index contains the value of end index(0 based indexing is used). If the key does not exist in the array then return -1 for both start and end index in this case.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(n)<br><strong>Expected Auxiliary Space:</strong> O(1).</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ n ≤ 10<sup>6</sup><br>1 &lt;= arr[i] , key &lt;= 10<sup>9</sup>&nbsp;</span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Data Structures</code>&nbsp;