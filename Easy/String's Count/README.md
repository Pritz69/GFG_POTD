<h2><a href="https://www.geeksforgeeks.org/problems/count-of-strings-that-can-be-formed-using-a-b-and-c-under-given-constraints1135/1">String's Count</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a length <strong>n</strong>, count the number of strings of length <strong>n</strong> that can be made using <strong>a</strong>, <strong>b</strong> and <strong>c</strong> with at-most one <strong>b</strong> and two <strong>c</strong>&nbsp;allowed.</span></p>
<p><strong><span style="font-size: 18px;">Example 1:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> n = 1</span>
<span style="font-size: 18px;"><strong>Output:</strong> 3
<strong>Explanation:</strong> Possible strings are: "a",
"b" and "c"</span>
</pre>
<p><strong><span style="font-size: 18px;">Example 2:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> n = 3
<strong>Output:</strong> 19
<strong>Explanation:</strong> Number of strings with 3 
occurrances of a: 1
2-a and 1-b: 3
2-a and 1-c: 3
1-a, 1-b and 1-c: 6
1-a and 2-c: 3
1-b and 2-c: 3
So, total number of strings of length 3
is 1 + 3 + 3 + 6 + 3 + 3 = 19
</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:&nbsp;&nbsp;</strong><br>You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>countStr</strong><strong>()</strong>&nbsp;which takes the <strong>n</strong></span><span style="font-size: 18px;"><strong> </strong>as inputs and returns the <strong>total number</strong> of valid strings.<br><br><strong>Expected Time Complexity:</strong>&nbsp;O(1)<br><strong>Expected Auxiliary Space:</strong>&nbsp;O(1)<br><br><strong>Constraints:</strong><br>1 ≤ n ≤ 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>Google</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Strings</code>&nbsp;<code>Dynamic Programming</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;