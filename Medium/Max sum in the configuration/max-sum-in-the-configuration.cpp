//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
/*You are required to complete this method*/
class Solution {
  public:
    long long max_sum(int a[], int n) {
        
        long long elements_sum = 0, ans = 0;
        
        for(int i = 0; i < n; i++) {
            elements_sum += a[i];
            ans += (1LL*i*a[i]);
        }

        long long curr = ans;
        
        for(int last = n-1; last > 0; last--){
            
            int last_element = a[last];
            long long change = elements_sum - 1LL * n * last_element;
            
            curr += change;
            
            if(curr > ans) ans = curr;
        }
        
        return ans;
    }
};

//{ Driver Code Starts.
int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        int A[N];
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        Solution ob;
        cout << ob.max_sum(A, N) << endl;
        /*keeping track of the total sum of the array*/
    }
}

// } Driver Code Ends