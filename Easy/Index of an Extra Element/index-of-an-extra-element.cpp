//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int findExtra(int n, int arr1[], int arr2[]) {
        
        int index = n - 1;
        int start = 0, end = n - 2;
        
        while (start <= end) {
            int mid = (end - start) / 2 + start;
            if (arr2[mid] == arr1[mid])
                start = mid + 1;
            else {
                index = mid;
                end = mid - 1;
            }
        }

        return index;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int arr1[n], arr2[n - 1];
        for (int i = 0; i < n; i++) {
            cin >> arr1[i];
        }
        for (int i = 0; i < n - 1; i++) {
            cin >> arr2[i];
        }
        Solution obj;
        cout << obj.findExtra(n, arr1, arr2) << endl;
    }
}
// } Driver Code Ends