//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++
//  Class Solution to contain the method for solving the problem.
class Solution {
  public:
    // Function to determine if array arr can be split into three equal sum sets.
    vector<int> findSplit(vector<int>& arr) {
      int cnt=0;
      int sum=0;
      int k=0,j=-1;
      int n=arr.size();
      int total=accumulate(arr.begin(),arr.end(),0);
      if(total==0)return {0,0};
      if(total%3!=0)return {-1,-1};
      int target=total/3;
      for(int i=0;i<n;i++)
      {
           sum+=arr[i];
           if(sum==target)
           {
               sum=0;
               cnt++;
               if(j==-1)
               {
                    j=i;
               }
           }
      }
      if(cnt==3)
      {
          
          return {k,j};
      }
      return {-1,-1};
    }
};

//{ Driver Code Starts.

int main() {
    int test_cases;
    cin >> test_cases;
    cin.ignore();
    while (test_cases--) {
        string input;
        vector<int> arr;

        // Read the array from input line
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        // Solution instance to invoke the function
        Solution ob;
        vector<int> result = ob.findSplit(arr);

        // Output result
        if (result[0] == -1 && result[1] == -1) {
            cout << "false" << endl;
        } else {
            cout << "true" << endl;
        }
    }
    return 0;
}

// } Driver Code Ends