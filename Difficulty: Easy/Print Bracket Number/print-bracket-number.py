#User function Template for python3
class Solution:
	def bracketNumbers(self, str):
		# code here
        ans = []# Initialize an empty list to store the result
        
        open_count = 1 # counter for open brackets
        st = [] # Initiallize an empty stack
        for char in str: # iterate over each character in the input string
            if char =='(': # if the character is an open bracket
            
                st.append(open_count) # Push the current open bracket count in the stack 
                ans.append(open_count)# add the current open bracker count to the result list
                open_count +=1 # Increment the open bracket
            
            elif char ==')':# if the character is a close bracket
                ans.append(st.pop())# pop the top element from the stack
                # and add to the result list
                
        return ans # return the result list

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends