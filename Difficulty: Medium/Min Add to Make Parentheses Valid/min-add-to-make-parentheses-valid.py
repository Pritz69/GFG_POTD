class Solution:
    def minParentheses(self, s):
        # code here
        #()))()()((())
        st=[]
        ans=0
        for x in s :
            if x=="(" :
                st.append(x)
            else :
                if st :
                    st.pop()
                else :
                    ans +=1
        return ans + len(st)
            