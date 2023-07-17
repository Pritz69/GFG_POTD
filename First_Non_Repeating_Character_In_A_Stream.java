//TLE
// Python gets accepted :-
from collections import OrderedDict

class Solution:
    def FirstNonRepeating(self, A):
        # Code here
        out = ""
        dic = OrderedDict()
        for i in A:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            s = 0
            for i, j in dic.items():
                if j == 1:
                    out += i
                    s = 1
                    break
            if s == 0:
                out += '#'
        return out

  
class Solution
{
    public String FirstNonRepeating(String A)
    {
        // code here
        LinkedHashMap<Character,Integer> h=new LinkedHashMap<Character,Integer>();
        String s="";
        for(int i=0;i<A.length();i++)
        {
            int x=h.getOrDefault(A.charAt(i),0);
            h.put(A.charAt(i),x+1);
            int f=0;
            for(char ch: h.keySet())
            {
                if (h.get(ch)==1)
                {
                    s += ch;
                    f=1;
                    break;
                }
            }
            if(f==0)
            {
                s +="#";
            }
        }
        return s;
    }
}
