class Solution:
    def romanToDecimal(self, s): 
        # code here
        d={"I" : 1, "V":5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        ans=0
        st=[]
        for x in s :
            if st and d[st[-1]] < d[x] :
                v=d[x]-d[st[-1]]
                st.pop()
                ans += v
            else :
                st.append(x)
        for x in st :
            ans += d[x]
        return ans