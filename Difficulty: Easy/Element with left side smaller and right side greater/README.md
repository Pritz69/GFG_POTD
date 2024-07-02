<h2><a href="https://www.geeksforgeeks.org/problems/unsorted-array4925/1">Element with left side smaller and right side greater</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an unsorted array of size <strong>N</strong>. Find the first element in array such that all of its&nbsp;left elements are smaller and all right elements to it are greater than it.</span></p>

<p><span style="font-size:18px"><strong>Note:</strong> Left and right side elements can be equal to required element. And extreme elements cannot be required element.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 4
A[] = {4, 2, 5, 7}
<strong>Output:</strong>
5
<strong>Explanation:
</strong>Elements on left of 5 are smaller than 5
and on right of it are greater than 5.</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 3
A[] = {11, 9, 12}
<strong>Output:</strong>
-1</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>findElement()</strong>&nbsp;which takes the array <strong>A[]</strong> and its size <strong>N</strong><strong> </strong>as inputs and returns the required element. If no such element present in array then return -1.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N)<br>
<strong>Expected Auxiliary Space:</strong> O(N)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
3 &lt;= N &lt;= 10<sup>6</sup><br>
1 &lt;= A[i] &lt;= 10<sup>6</sup></span></p>
</div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Zoho</code>&nbsp;<code>Amazon</code>&nbsp;<code>OYO Rooms</code>&nbsp;<code>Intuit</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Data Structures</code>&nbsp;