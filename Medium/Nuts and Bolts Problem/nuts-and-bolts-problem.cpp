//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
// User function template fo


class Solution {
    int findIndex(char c, int i, int n, char *arr) {
        while (i < n) {
            if (arr[i] == c)
                return i;
            i++;
        }
        return -1;
    }
  public:
    void matchPairs(int n, char nuts[], char bolts[]) {
        vector<char> order = {'!', '#', '$', '%', '&', '*', '?', '@', '^'};
        int last1 = 0, last2 = 0;
        for (auto &it : order) {
            int idx1 = findIndex(it, last1, n, nuts);
            int idx2 = findIndex(it, last2, n, bolts);
            if (idx1 >= 0) {
                swap(nuts[idx1], nuts[last1]);
                last1++;
            }
            if (idx2 >= 0) {
                swap(bolts[idx2], bolts[last2]);
                last2++;
            }
        }
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        char nuts[n], bolts[n];
        for (int i = 0; i < n; i++) {
            cin >> nuts[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> bolts[i];
        }
        Solution ob;
        ob.matchPairs(n, nuts, bolts);
        for (int i = 0; i < n; i++) {
            cout << nuts[i] << " ";
        }
        cout << "\n";
        for (int i = 0; i < n; i++) {
            cout << bolts[i] << " ";
        }
        cout << "\n";
    }
    return 0;
}

// } Driver Code Ends