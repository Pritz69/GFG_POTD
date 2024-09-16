//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int maxLength(string str) {
        // Get the length of the input string
        int n = str.length();
        
        // Stack to store indices of parentheses
        stack<int> st;
        
        // Initial push of -1 to handle edge cases (e.g., valid string starting from index 0)
        st.push(-1);
        
        // Variable to store the maximum valid length
        int ans = 0;
        
        // Traverse the input string character by character
        for(int i = 0; i < n; ++i) {
            // If the current character is '(', push its index onto the stack
            if(str[i] == '(') {
                st.push(i);
            }
            // If the current character is ')', attempt to close the most recent '('
            else {
                st.pop(); // Pop the top element (an opening parenthesis index)
                
                // If the stack becomes empty, it means we have unmatched closing parenthesis
                if(st.empty()) {
                    // Push the index of the unmatched closing parenthesis as a new "starting point"
                    st.push(i);
                }
                // Otherwise, calculate the length of the valid substring
                else {
                    // Calculate the length between current index and the top of the stack
                    ans = max(ans, i - st.top());
                }
            }
        }
        
        // Return the maximum length of valid parentheses found
        return ans;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        string S;
        cin >> S;

        Solution ob;
        cout << ob.maxLength(S) << "\n";
    }
    return 0;
}
// } Driver Code Ends