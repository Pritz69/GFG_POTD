class Solution:
    def canServe(self, arr):
        # code here 
        #10 --> one 5 rupee coin 
        #20 --> one 10 rupee coin, one 5 rupee coin  OR  three 5 rupee coin
        c5=0
        c10=0
        c20=0
        for coin in arr  :
            if coin==5 :
                c5 +=1
            elif coin==10 :
                if c5==0 : 
                    return False
                c5 -=1
                c10 +=1
            else :
                if c5 >=1 and c10 >=1 :
                    c5 -=1
                    c10 -=1
                elif c5 >= 3 :
                    c5 -=3
                else :
                    return False
                c20 +=1
        return True   