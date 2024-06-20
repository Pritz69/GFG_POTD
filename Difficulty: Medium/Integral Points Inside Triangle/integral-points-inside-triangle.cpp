//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    long long int InternalCount(long long int p[], long long int q[],
                                long long int r[]) {
        // code here
        // Formula for calculating area :

// Area=21​∣x1​(y2​−y3​)+x2​(y3​−y1​)+x3​(y1​−y2​)∣
        long long area = abs(p[0]*(q[1]-r[1]) + q[0]*(r[1]-p[1]) + r[0]*(p[1]-q[1]))/2;
        long long boundaryPoint1 = __gcd(abs(p[0]-q[0]), abs(p[1]-q[1])) + 1;
        long long boundaryPoint2 = __gcd(abs(p[0]-r[0]), abs(p[1]-r[1])) + 1;
        long long boundaryPoint3 = __gcd(abs(r[0]-q[0]), abs(r[1]-q[1])) + 1;
        
        // according to pick's theorem
        /*
        Area = I + B/2 - 1
        => I = Area - B/2 + 1
        where :
        Area is area of triangle
        I is the number of interior lattice (integral) points
        B is the number of boundary lattice points
        */
        long long B = boundaryPoint1 + boundaryPoint2 + boundaryPoint3 - 3;
        long long I = (area - B/2 + 1);
        return I;
        
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        long long int p[2], q[2], r[2];
        cin >> p[0] >> p[1] >> q[0] >> q[1] >> r[0] >> r[1];
        Solution ob;
        long long int ans = ob.InternalCount(p, q, r);
        cout << ans << "\n";
    }
}
// } Driver Code Ends