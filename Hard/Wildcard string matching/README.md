<h2><a href="https://www.geeksforgeeks.org/problems/wildcard-string-matching1126/1">Wildcard string matching</a></h2><h3>Difficulty Level : Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given two strings <strong>wild</strong> and <strong>pattern</strong>. Determine if the given two strings can be matched given that, <strong>wil</strong><strong>d</strong> string may contain <strong>*</strong> and <strong>?</strong> but string <strong>pattern </strong>will not.&nbsp;*<strong>&nbsp;</strong>and <strong>?</strong> can be converted to another character according to the following rules:</span></p>
<pre><span style="font-size: 18px;">* --&gt; This character in string wild can be replaced by any sequence of characters, it can also be replaced by an empty string.
? --&gt; This character in string wild can be replaced by any one character.</span></pre>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: <br></strong>wild = ge*ks<br>pattern = geeks
<strong>Output: </strong>Yes
<strong>Explanation:</strong> Replace the '*' in wild string 
with 'e' to obtain pattern "geeks".</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: <br></strong>wild =<strong> </strong>ge?ks*<br>pattern = geeksforgeeks
<strong>Output:</strong> Yes
<strong>Explanation:</strong> Replace '?' and '*' in wild string with
'e' and 'forgeeks' respectively to obtain pattern 
"geeksforgeeks"
</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You don't need to read&nbsp;input or print anything. Your task is to&nbsp;complete the function <strong>match() </strong>which takes<strong>&nbsp;</strong>the string <strong>wild</strong> and <strong>pattern</strong> as input parameters and returns <strong>true</strong> if the string <strong>wild </strong>can be made equal to the string <strong>pattern</strong>, otherwise, returns&nbsp;<strong>false</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(length of wild string *&nbsp;length of pattern string)<br><strong>Expected Auxiliary Space:</strong> O(length of wild string *&nbsp;length of pattern string)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= length of the two string &lt;= 10^3</span><span style="font-size: 18px;">&nbsp;</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>Ola Cabs</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Strings</code>&nbsp;<code>Data Structures</code>&nbsp;