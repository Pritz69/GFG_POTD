//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
//User function template for C++
class Solution{
public:	
	// Converts arr[0..n-1] to reduced form.
	int binarySearch(vector<int> &temp,int num){

     int start=0, end=temp.size()-1;

     int mid=start+(end-start)/2;

     while(start<=end){

         if(temp[mid]==num)

            return mid;

        else if(temp[mid]>num)

            end=mid-1;

        else if(temp[mid]<num)

            start=mid+1;

            

        mid=start+(end-start)/2;

     }

     

     return 0;

 }

 void convert(int arr[], int n) {

     // code here

     //insert the array into vector so that the orginal will remain same

     vector<int> temp(arr, arr+n);

     sort(temp.begin(),temp.end());

     

     for(int i=0;i<n;i++)

     {

         int ind=binarySearch(temp,arr[i]);

         arr[i]=ind;

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
        int arr[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        Solution ob;
        ob.convert(arr, n);
        for (int i = 0; i < n; i++) {
            cout << arr[i] << " ";
        }
        cout << "\n";
    }
    return 0;
}

// } Driver Code Ends
