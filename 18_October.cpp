class Solution{
	
	public:
	vector<int> downwardDigonal(int N, vector<vector<int>> A)
	{
		// Your code goes here
		map<int,vector<int>>m;
		for(int i=0;i<N;i++)
		{
		    for(int j=0;j<N;j++)
		    {
		        m[i+j].push_back(A[i][j]);
		    }
		}
		vector<int>vc;
		for(int i=0;i<=N+N;i++)
		{
		    for(int x:m[i])
		    {
		        vc.push_back(x);
		    }
		}
		return vc;
	}

};
