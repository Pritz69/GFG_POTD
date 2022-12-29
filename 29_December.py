class Solution:
    def asteroidCollision(self, N, asteroids):
        # Code here
        st=[]
        for i in asteroids:
            if i>0:
                st.append(i)
            else:
                if not st:
                    st.append(i)
                elif st[-1]<0:
                    st.append(i)
                else:
                    while st and st[-1]>0 and st[-1]<abs(i):
                        st.pop()
                    if not st:
                        st.append(i)
                    else:
                        if st[-1]==abs(i):
                            st.pop()
                        else:
                            if st[-1]<0:
                                st.append(i)
        return st
