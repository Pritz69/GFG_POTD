//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
  public:
  int findSum(int r1, int c1, int r2, int c2, int n, int m, vector<vector<int>> &pref){
	int sum = pref[r2][c2];
	if((c1 - 1) >= 0){
		sum -= pref[r2][c1 - 1];
	}
	if((r1 - 1) >= 0){
		sum -= pref[r1 - 1][c2];
	}
	if((c1 - 1) >= 0 && (r1 - 1) >= 0){
		sum += pref[r1 - 1][c1 - 1];
	}
	return sum;
  }
  
  vector<vector<int>> sumZeroMatrix(vector<vector<int>> a){
      int n = a.size(), m = a[0].size();
      vector<vector<int>> pref(n, vector<int>(m, 0));
      for(int i = 0; i < n; i++){ //right side
          for(int j = 0; j < m; j++){
              pref[i][j] = a[i][j];
              if((j - 1) >= 0){
				pref[i][j] += pref[i][j - 1];
              }
          }
      }
      for(int j = 0; j < m; j++){ //bottom
          for(int i = 0; i < n; i++){
              if((i - 1) >= 0){
                  pref[i][j] += pref[i - 1][j];
              }
          }
      }
      int ans = 0;
      vector<int> sub_matrix(4, 0);
      for(int r1 = 0; r1 < n; r1++){
          for(int c1 = 0; c1 < m; c1++){
              for(int r2 = r1; r2 < n; r2++){
                  for(int c2 = c1; c2 < m; c2++){
					int sum = findSum(r1, c1, r2, c2, n, m, pref);
					if(sum == 0){
						int submatrixSize = (r2 - r1 + 1)*(c2 - c1 + 1);
						if(submatrixSize > ans){
						    ans = submatrixSize;
						    sub_matrix = {r1, r2, c1, c2};
						}else if(submatrixSize == ans){
						    if(c1 < sub_matrix[2]){
						        sub_matrix = {r1, r2, c1, c2};
						    }else if(c1 == sub_matrix[2] and r2 - r1 + 1 > sub_matrix[1] - sub_matrix[0] + 1){
						        sub_matrix = {r1, r2, c1, c2};
						    }else if(c1 == sub_matrix[2] and r2 - r1 + 1 == sub_matrix[1] - sub_matrix[0] + 1 and r1 < sub_matrix[0]){
						        sub_matrix = {r1, r2, c1, c2};
						    }
						}
					}
				}
			}
		}
	}
	if(ans == 0){
	    vector<vector<int>> result = {{}};
	    return result;
	}
	int first_row = sub_matrix[0];
	int last_row = sub_matrix[1];
	int first_col = sub_matrix[2];
	int last_col = sub_matrix[3];
	vector<vector<int>> ans_mat(last_row - first_row + 1, vector<int>(last_col - first_col + 1, 0));
	for(int i = first_row; i <= last_row; i++){
	    for(int j = first_col; j <= last_col; j++){
	        ans_mat[i - first_row][j - first_col] = a[i][j];
	    }
	}
	return ans_mat;
  }
};


//{ Driver Code Starts.




int main(){
    int t;
    cin>>t;
    while(t--){
        int n,m;
        cin>>n>>m;
        
        vector<vector<int>> a(n,vector<int>(m));
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                cin>>a[i][j];
            }
        }
        Solution ob;
        vector<vector<int>> ans = ob.sumZeroMatrix(a);
        if(ans.size() == 0){
            cout<<-1<<endl;
        }
        else{
            for(int i=0;i<ans.size();i++){
                for(int j=0;j<ans[0].size();j++){
                    cout<<ans[i][j]<<" ";
                }
                cout<<endl;
            }
        }
    }
    return 0;
}
// } Driver Code Ends