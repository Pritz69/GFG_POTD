//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function template for C++

class Solution {
  public:
    int majorityElement(vector<int>& arr) {
    int count = 1;
    int element = arr[0]; 

    for(int i = 1; i < arr.size(); i++) {
        if(count == 0) {
            element = arr[i];
            count = 1;
        }
        else if(element == arr[i]) {
            count++;
        }
        else {
            count--;
        }
    }

    count = 0;
    for(int i = 0; i < arr.size(); i++) {
        if(element == arr[i]) count++;
    }

    return (arr.size()+2 ) / 2 <= count ? element : -1;
}
};


//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        int n;
        vector<int> a, b;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int num;
        while (ss >> num)
            a.push_back(num);

        Solution obj;
        cout << obj.majorityElement(a) << endl;
        cout << "~" << endl;
    }

    return 0;
}

// } Driver Code Ends