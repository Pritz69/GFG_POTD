#User function Template for python3

class Solution:    
    def countPairs(self,arr, n): 
         # Your code goes here
        def merge(arr,l,m,h) :
            t=[]
            c=0
            le=l
            ri=m+1
            while le<=m and ri<=h :
                if arr[le] <= arr[ri] :
                    t.append(arr[le])
                    le +=1
                else :
                    c += (m-le +1)
                    t.append(arr[ri])
                    ri +=1
            while le<=m :
                t.append(arr[le])
                le +=1
            while ri<=h :
                t.append(arr[ri])
                ri +=1
            for i in range(l,h+1) :
                arr[i]=t[i-l]
            return c
        def mergesort(arr,l,h) :
            cnt=0
            if l >= h :
                return cnt
            m=(l+h)//2
            cnt += mergesort(arr,l,m)
            cnt += mergesort(arr,m+1,h)
            cnt += merge(arr,l,m,h)
            return cnt
            
        for i in range(n) :
            arr[i]=i*arr[i]
        return mergesort(arr,0,n-1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob= Solution()
        print(ob.countPairs(a, n))

        T -= 1


if __name__ == "__main__":
    main()
    
# } Driver Code Ends