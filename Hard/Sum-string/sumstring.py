#User function Template for python3
class Solution:
    def isSumString (ob,S):
        def check_string(i,j,k):
            if k == len(S):
                return True
            elif k > len(S):
                return False
            string_1 = int(S[i:j])
            string_2 = int(S[j:k])
            new_string = str(string_1 + string_2)
            
            if not S[k:].startswith(new_string):
                return False
            return check_string(j, k, k+len(new_string))
            
        for i in range(1,len(S)):
            for j in range(i+1,len(S)):
                if check_string(0,i,j):
                    return 1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        
        print(ob.isSumString(S))
# } Driver Code Ends