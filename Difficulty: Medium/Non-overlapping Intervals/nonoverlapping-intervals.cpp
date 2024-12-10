//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    int minRemoval(vector<vector<int>> &intervals) {
        // code here
        int n = intervals.size();
        sort(intervals.begin(), intervals.end());
        
        int res = 0;
        int en = intervals[0][1];
        for(int i = 1; i < n; i++) {
            if(intervals[i][0] == intervals[i - 1][0]) {
                res++;
            }
            else {
                if(intervals[i][0] >= en) {
                    en = intervals[i][1];
                }
                else {
                    en = min(en, intervals[i][1]);
                    res++;
                }
            }
        }
        
        return res;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;

        vector<vector<int>> intervals(N, vector<int>(2));
        for (int i = 0; i < N; i++) {
            cin >> intervals[i][0] >> intervals[i][1];
        }
        Solution obj;
        cout << obj.minRemoval(intervals) << endl;

        cout << "~"
             << "\n";
    }
    return 0;
}
// } Driver Code Ends