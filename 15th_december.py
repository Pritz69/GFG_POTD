#User function Template for python3

class Solution:
    def BalancedString(self,N):
        N_u = N
        temp = []
        alphab = ""
        if N>26:
            N_u = N%26
            alphab="abcdefghijklmnopqrstuvwxyz"*(N//26)
        
        
        if(N%2 == 0):
            for i in range(N_u//2):
                temp.append(chr(97+i))
            for i in range(N_u//2,N_u):
                temp.append(chr(122-N_u+1+i))
        else:
            if(sum(list(int(i) for i in str(N)))%2 == 0):
                for i in range((N_u+1)//2):
                    temp.append(chr(97+i))
                for i in range((N_u-1)//2+1,N_u):
                    temp.append(chr(122-N_u+1+i))
                    
                    
            else:
                for i in range((N_u-1)//2):
                    temp.append(chr(97+i))
                for i in range((N_u+1)//2-1,N_u):
                    temp.append(chr(122-N_u+1+i))
        return alphab+"".join(str(i) for i in temp)
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        
        ob=Solution()
        print(ob.BalancedString(N))
# } Driver Code Ends
