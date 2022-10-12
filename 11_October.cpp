class Solution{
public:
    string decodedString(string s){
        int n=s.size(), cnt=0;
        stack<string> st;
        string ans;
        for(int i=0; i<n; i++) {
            if(s[i]!=']') {
                string temp;
                temp+=s[i];
                st.push(temp); continue;
            }
            string curr;
            while(!st.empty()&&st.top()!="[") {
                curr+=st.top();
                st.pop();
            }
            st.pop();
            string count;
            while(!st.empty()&&st.top()>="0"&&st.top()<="9") {count+=st.top(); st.pop();}
            reverse(count.begin(), count.end());
            cnt=stoi(count);
            string str;
            while(cnt--) {
                str+=curr;
            }
            st.push(str);
        }
        while(!st.empty()) {
            ans+=st.top(); st.pop();
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
