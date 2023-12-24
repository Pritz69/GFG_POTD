<h2><a href="https://www.geeksforgeeks.org/problems/buy-maximum-stocks-if-i-stocks-can-be-bought-on-i-th-day/1">Buy Maximum Stocks if i stocks can be bought on i-th day</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">In a stock market, there is a product with its infinite stocks. The stock prices are given for&nbsp;<strong>N</strong>&nbsp;days, where <strong>price[i]</strong> denotes the price of the stock on the i<sup>th</sup>&nbsp;day.<br>There is a rule that a customer can buy at most i stock on the i<sup>th</sup>&nbsp;day.<br>If the customer has an amount of&nbsp;<strong>k</strong>&nbsp;amount of money initially. The task is to&nbsp;find out the maximum number of stocks a customer can buy.&nbsp;</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>price = [10,7,19]
k = 45
<strong>Output: <br></strong>4
<strong>Explanation:</strong> <br>A customer purchases 1 stock on day 1, 2 stocks on day 2 and 1 stock on day 3 for 10, 7 * 2 = 14 and 19 respectively. Hence, total amount is 10 + 14 + 19 = 43 and number of stocks purchased is 4.</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: 
</strong>price = [7,10,4]
k = 100
<strong>Output: <br></strong>6<br><strong>Explanation:</strong><br>Buy on all 3 days.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:&nbsp;&nbsp;</strong><br>You don't need to read input or print anything. Your task is to complete the function <strong>buyMaximumProducts</strong><strong>()</strong>&nbsp;which takes an array&nbsp;<strong>price&nbsp;</strong>and an integer&nbsp;<strong>k</strong>&nbsp;and returns an integer as output.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(NlogN)<br><strong>Expected Auxiliary Space:</strong> O(N)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= N &lt;= 10<sup>4</sup><br>1 &lt;= price[i] &lt;= 10<sup>4</sup><br>1 &lt;= k &lt;= 10<sup>4</sup></span><br>&nbsp;</p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Data Structures</code>&nbsp;