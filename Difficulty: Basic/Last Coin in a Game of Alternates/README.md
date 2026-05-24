<h2><a href="https://www.geeksforgeeks.org/problems/last-coin-in-a-game-of-alternates/1">Last Coin in a Game of Alternates</a></h2><h3>Difficulty Level : Difficulty: Basic</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p data-pm-slice="0 0 []"><span style="font-size: 18.6667px;">Given an array integer<strong> arr[]</strong> , representing the values of coins arranged in a row.</span></p>
<ul>
<li data-pm-slice="0 0 []"><span style="font-size: 18.6667px;">Two players play a game by picking coins alternately.</span></li>
<li data-pm-slice="0 0 []"><span style="font-size: 18.6667px;">At each turn, a player can pick a coin from either the beginning or the end of the array. Both players follow a greedy strategy, i.e., they always pick the coin with the maximum value among the two available ends.</span></li>
<li data-pm-slice="0 0 []"><span style="font-size: 18.6667px;">The game continues until only one coin remains.</span></li>
</ul>
<p data-pm-slice="0 0 []"><span style="font-size: 18.6667px;">Find the value of the <strong>last remaining coin</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong style="font-size: 18px;">Input : </strong><span style="font-size: 18px;">arr[] = [5, 3, 1, 6, 9]
</span><strong style="font-size: 18px;">Output : </strong><span style="font-size: 18px;">1
</span><strong style="font-size: 18px;">Explanation:
</strong><span style="font-size: 18px;">Players always pick the larger coin from the two ends.
Pick 9, remaining array: [5, 3, 1, 6]
Pick 6, remaining array: [5, 3, 1]
Pick 5, remaining array: [3, 1]
Pick 3, remaining array: [1]
Final Output: 1</span></span></pre>
<pre><span style="font-size: 18px;"><strong style="font-size: 18px;">Input : </strong><span style="font-size: 18px;">arr[] = [5, 9, 2, 5]</span><strong style="font-size: 18px;">
Output : </strong><span style="font-size: 18px;">2<br></span><strong style="font-size: 18px;">Explanation:<br></strong><span style="font-size: 18px;">Players always pick the larger coin from the two ends.
Pick 5, remaining array: [9, 2, 5]
Pick 9, remaining array: [2, 5]
Pick 5, remaining array: [2]
Final Output: 2</span></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input : </strong>arr[] = [11]<strong>
Output : </strong>11<br><strong>Explanation:<br></strong>Only one coin is present in the array, so no moves are made.
Final Output: 11</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints :<br></strong></span><span style="font-size: 18px;">1 ≤ arr.size() ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>6</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>two-pointer-algorithm</code>&nbsp;<code>Arrays</code>&nbsp;<code>Greedy</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;