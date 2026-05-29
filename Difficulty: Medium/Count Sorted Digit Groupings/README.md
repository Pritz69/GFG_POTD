<h2><a href="https://www.geeksforgeeks.org/problems/count-digit-groupings-of-a-number1520/1">Count Sorted Digit Groupings</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given a string <strong>s</strong> consisting of digits, you can split it into <strong>contiguous </strong>substrings (sub-groups).&nbsp;</span><span style="font-size: 18px;">For example, the string "112" can be split as: ["1","1","2"], ["11","2"], ["1","12"], and ["112"].</span></p>
<p><span style="font-size: 18px;">A grouping is considered valid if the sums of digits of the sub-groups form a <strong>non-decreasing</strong> sequence from left to right.</span></p>
<p><span style="font-size: 18px;">Determine the <strong>total </strong>number of such valid groupings for the given string.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:&nbsp;</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>s = "1119"
<strong>Output: </strong>7
<strong>Explanation: <br></strong></span><span style="font-size: 18px;">One valid grouping is ["1", "11", "9"].
The sum of digits of the first sub-group ("1") is 1,
for the second sub-group ("11"), it is 2,
and for the third sub-group ("9"), it is 9.
Since the sums are in non-decreasing order (1 ≤ 2 ≤ 9), this is a valid grouping.
The other valid groupings are:
["1", "119"], ["1", "1", "19"], ["1", "1", "1", "9"], ["11", "19"], ["111", "9"], and ["1119"].
Thus, the total number of valid groupings is 7.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>s = "12"
<strong>Output: </strong>2
<strong>Explanation: <br></strong>["1","2"] and ["12"] are two valid groupings.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ s.size() ≤ 100<br>s[i]<sub>&nbsp;</sub>∈ {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}</span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Dynamic Programming</code>&nbsp;<code>Algorithms</code>&nbsp;