<h2><a href="https://www.geeksforgeeks.org/problems/variation-in-nim-game4317/1">Modified Game of Nim</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">You are given an array <strong>A</strong>&nbsp;of <strong>n&nbsp;</strong>elements. There are two players player 1&nbsp;and player 2.<br>A player can choose any of element from an array and remove it. If the bitwise XOR of all remaining elements equals 0 after removal of the selected element, then that player loses. Find out the winner if player 1 starts the game and they both play&nbsp;their best.&nbsp;</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> <br>n = 3
A = [3, 3, 2]
<strong>Output:</strong> <br>2
<strong>Explaination:</strong> <br>Optimal removal of values are 3, 2, 3 sequentially. Then the array is empty. So player 2 wins.</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> <br>n = 2
A = [3, 3]
<strong>Output:</strong> <br>1
<strong>Explaination:</strong> <br>Since the xor of an array is already 0, player 1 wins.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You do not need to read input or print anything. Your task is to complete the function <strong>findWinner()</strong> which takes the number <strong>n</strong> and the array <strong>A</strong> as input parameters and returns an integer denoting the winner.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity: </strong>O(n)<br><strong>Expected Auxiliary Space:</strong> O(1)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ n ≤ 10<sup>5</sup><br>0 ≤ A[i] ≤ 10<sup>9</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Bit Magic</code>&nbsp;<code>Game Theory</code>&nbsp;<code>Data Structures</code>&nbsp;