from typing import List


class Solution:
    def finLength(self, N : int, color : List[int], radius : List[int]) -> int:
        # code here
        st=[]
        for x,y in zip(color,radius) :
            if st and st[-1]==[x,y] :
                st.pop()
            else :
                st.append([x,y])
        return len(st)
