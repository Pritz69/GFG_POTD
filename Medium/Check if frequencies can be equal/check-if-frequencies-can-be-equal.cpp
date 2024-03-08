//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++
class Solution{
public:
bool sameFreq(string s)
{
    // code here 
    int n = s.size();
    map<char,int> mp;
    for(auto it : s) mp[it]++;
    map<int,int> h;
 
   int mini = 1e7;
    for(auto it : mp){
        mini = min(it.second,mini);
      h[it.second]++;
    }
   
    if(h.size()==1) return true;
    if(h.size() ==2){
      
        for(auto it : h){
            int cnt = it.second;
            int mpfreq = it.first;
           if(cnt == 1){
               if(mpfreq == 1) return true;
               if(mpfreq == mini + 1) return true;
           }
            
        }
    }
    return false;
   
}
};

//{ Driver Code Starts.
int main(){
    int t;
    cin>>t;
    while(t--)
    {
        string s;
        cin>>s;
        Solution ob;
        cout<<ob.sameFreq(s)<<endl;
    }
}



// } Driver Code Ends