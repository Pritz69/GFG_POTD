from typing import List
class Solution:
    def is_possible_to_get_seats(self, n : int, m : int, seats : List[int]) -> bool:
        # code here
        available_seats = 0
        i = 0
        while i < m:
            prev = 0
            if i == 0:
                prev = 0
            else:
                prev = seats[i-1]
            nxt = 0
            if i == m-1:
                nxt = 0
            else:
                nxt = seats[i+1]
            
            if prev + nxt + seats[i] == 0:
                available_seats += 1
                i +=1
            i += 1
        
        return available_seats >= n
