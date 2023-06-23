int leastInterval(int N, int K, vector<char> &tasks) {
        
        map<char, int> m;
        for(int i=0;i<N; i++){
            m[tasks[i]]++;
        }
        int mx=INT_MIN;
        for(auto i: m){
            if(i.second > mx){
                mx = i.second;
            }
        }
        int ideal = (mx-1)*K;
        ideal+=(mx-1);
        for(auto x : m){
            ideal-=min(mx-1, x.second);
        }
        return tasks.size() + max(0,ideal);
    }
