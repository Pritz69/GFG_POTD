class Solution{   
public:
    int appleSequences(int n, int m, string arr){
        int maxlen=0;
        int end=0,start=0;
        int count=0;
        while(end<n)
        {
            if(arr[end]=='O') count++;
            while(start<n && count>m)
            {
                if(arr[start]=='O') count--;
                start++;
            }
            maxlen=max(maxlen,end-start+1);
            end++;
        }
        return maxlen;
    }
};
