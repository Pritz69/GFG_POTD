<h2><a href="https://www.geeksforgeeks.org/problems/search-pattern-rabin-karp-algorithm--141631/1">Search Pattern (Rabin-Karp Algorithm)</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given two strings, one is a <strong>text </strong>string and other is a <strong>pattern </strong>string. The task is to print the indexes of all the occurences of pattern string in the text string. For printing, Starting Index of a string should be taken as 1. The strings will only contain lowercase English alphabets (<strong>'a' </strong>to<strong> 'z'</strong>).</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input</strong>: 
text = "birthdayboy"<br>pattern = "birth"<br><strong>Output:</strong> <br>[1]
<strong>Explanation</strong>: <br>The string "birth" occurs at index 1 in text.</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
text = "geeksforgeeks"<br>pattern = "geek"
<strong>Output:</strong> <br>[1, 9]
<strong>Explanation</strong>: <br>The string "geek" occurs twice in text, one starts are index 1 and the other at index 9.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>search()&nbsp;</strong>which takes the string <strong>text</strong> and the string <strong>pattern</strong> as input and returns an array denoting the start indices (1-based) of substring pattern in the string text.&nbsp;</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity: </strong>O(|text| + |pattern|).<br><strong>Expected Auxiliary Space:&nbsp;</strong>O(1).</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1&lt;=|text|&lt;=5*10<sup>5</sup><br>1&lt;=|pattern|&lt;=|text|</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Microsoft</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Strings</code>&nbsp;<code>Pattern Searching</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;