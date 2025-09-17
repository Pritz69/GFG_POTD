class Solution:
    def decodedString(self, s):
        d_s=[] #decodedString
        for i in s:
            if i=="]":
                sub_string=""
                while d_s[-1] != '[':
                    sub_string = d_s.pop() + sub_string #prepend the character
                d_s.pop()
                
                repitation=''
                while d_s and d_s[-1].isdigit():
                    repitation = d_s.pop() + repitation 
                
                d_s.append(int(repitation) * sub_string)
                continue
            
            d_s.append(i)
        
        return ''.join(d_s)