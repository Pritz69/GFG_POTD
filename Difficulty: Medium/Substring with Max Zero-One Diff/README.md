<h2><a href="https://www.geeksforgeeks.org/problems/maximum-difference-of-zeros-and-ones-in-binary-string4111/1">Substring with Max Zero-One Diff</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given a binary string <strong>s</strong> consisting of 0s and 1s. Find the <strong>maximum difference</strong> of the number of <strong>0s</strong> and the number of <strong>1s</strong> (number of 0s – number of 1s) in a substring of the string.</span></p>
<p><span style="font-size: 18px;"><strong>Note:</strong> In the case of all 1s, the answer will be -1. </span></p>
<p><strong><span style="font-size: 18px;">Examples:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input</strong> : s = "11000010001" 
<strong>Output</strong> : 6 
<strong>Explanatio:</strong> From index 2 to index 9, there are 7 0s and 1 1s, so number of 0s - number of 1s is 6. </span></pre>
<pre><span style="font-size: 18px;"><strong>Input:</strong> s = "111111"</span>
<span style="font-size: 18px;"><strong>Output:</strong> -1
<strong>Explanation:</strong> s contains 1s only </span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong></span><br><span style="font-size: 18px;">1 ≤ s.size() ≤ 10<sup>5</sup><br></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Strings</code>&nbsp;<code>Dynamic Programming</code>&nbsp;<code>Kadane</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;