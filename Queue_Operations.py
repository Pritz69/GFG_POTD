#User function Template for python3
class Solution:
    # Function to insert element into the queue
    def insert(self, q, k): 
        #code here
        q.append(k)
     
    # Function to find frequency of an element
    # return the frequency of k
    def findFrequency(self, q, k):
        # code here
        c=0
        for x in q :
            if x==k :
                c +=1
        return c
