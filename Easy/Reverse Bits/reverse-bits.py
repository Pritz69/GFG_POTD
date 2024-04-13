#User function Template for python3
class Solution:
    def reversedBits(self, x):
       
        binary_x = bin(x)[2:]  
        
        binary_x = '0' * (32 - len(binary_x)) + binary_x
      
        reversed_binary_x = binary_x[::-1]
        
        ans = int(reversed_binary_x, 2)
        
        return ans




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends