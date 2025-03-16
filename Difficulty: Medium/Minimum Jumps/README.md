<h2><a href="https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1">Minimum Jumps</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">You are given an array <strong>arr[]</strong> of non-negative numbers. Each number tells you the <strong>maximum number of steps</strong> you can jump forward from that position.</span></p>
<p><span style="font-size: 14pt;">For example:</span></p>
<ul>
<li><span style="font-size: 18.6667px;">If <strong>arr[i] = 3</strong>, you can jump to index <strong>i + 1</strong>, <strong>i + 2</strong>, or <strong>i + 3</strong> from position <strong>i</strong>.</span></li>
<li><span style="font-size: 14pt;">If&nbsp;<strong>arr[i] = 0</strong>, you <strong>cannot jump forward</strong> from that position.</span></li>
</ul>
<p><span style="font-size: 14pt;">Your task is to find the <strong>minimum number of jumps</strong> needed to move from the <strong>first</strong> position in the array to the <strong>last</strong> position.</span></p>
<p><span style="font-size: 14pt;"><strong>Note:&nbsp; </strong>Return <strong>-1</strong> if you can't reach the end of the array.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples :&nbsp;</strong> </span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
<strong>Output:</strong> 3 
<strong>Explanation: </strong>First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last. </span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr = [1, 4, 3, 2, 6, 7]<br><strong>Output:</strong> 2 
<strong>Explanation: </strong>First we jump from the 1st to 2nd element and then jump to the last element.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr = [0, 10, 20]<br><strong>Output:</strong> -1
<strong>Explanation: </strong>We cannot go anywhere from the 1st element.
</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>2 ≤ arr.size() ≤ 10<sup>4<br></sup>0 ≤ arr[i] ≤ 10<sup>4</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Moonfrog Labs</code>&nbsp;<code>Flipkart</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>Housing.com</code>&nbsp;<code>Walmart</code>&nbsp;<code>Adobe</code>&nbsp;<code>Google</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Greedy</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;