//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
public:
    int mergeAndCount(vector<int>& arr, vector<int>& temp, int left, int mid, int right) {
        int i = left;     // Starting index for left subarray
        int j = mid + 1;  // Starting index for right subarray
        int k = left;     // Starting index for temp array
        int invCount = 0; // Count of inversions

        // Merge the two subarrays and count cross-inversions
        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
                invCount += (mid - i + 1); // Count inversions
            }
        }

        // Copy remaining elements of left subarray (if any)
        while (i <= mid) {
            temp[k++] = arr[i++];
        }

        // Copy remaining elements of right subarray (if any)
        while (j <= right) {
            temp[k++] = arr[j++];
        }

        // Copy merged elements back into the original array
        for (int i = left; i <= right; i++) {
            arr[i] = temp[i];
        }

        return invCount;
    }

    int mergeSortAndCount(vector<int>& arr, vector<int>& temp, int left, int right) {
        int invCount = 0;
        if (left < right) {
            int mid = left + (right - left) / 2;

            // Count inversions in left subarray
            invCount += mergeSortAndCount(arr, temp, left, mid);

            // Count inversions in right subarray
            invCount += mergeSortAndCount(arr, temp, mid + 1, right);

            // Count cross-inversions during merge
            invCount += mergeAndCount(arr, temp, left, mid, right);
        }
        return invCount;
    }

    int inversionCount(vector<int>& arr) {
        int n = arr.size();
        vector<int> temp(n);
        return mergeSortAndCount(arr, temp, 0, n - 1);
    }
};


//{ Driver Code Starts.

int main() {

    int T;
    cin >> T;
    cin.ignore();
    while (T--) {
        int n;
        vector<int> a;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int num;
        while (ss >> num)
            a.push_back(num);
        Solution obj;
        cout << obj.inversionCount(a) << endl;
        cout << "~" << endl;
    }

    return 0;
}

// } Driver Code Ends