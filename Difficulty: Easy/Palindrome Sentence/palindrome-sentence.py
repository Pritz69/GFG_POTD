class Solution:
	def isPalinSent(self, s):
		# code here
		ns=""
		for x in s :
		    if 65 <= ord(x) and ord(x) <= 90 : 
		        ns += chr(ord(x)+32)
		    elif 97 <= ord(x) and ord(x)<=122:
		        ns += x
		    elif 48 <= ord(x) and ord(x) <= 57 :
		        ns +=x
	    l,r=0,len(ns)-1
	    #print(ns)
	    while l <= r :
	        if ns[l] != ns[r] :
	            return False
	        l +=1
	        r -=1
	    return True