#User function Template for python3

class Solution:
    def multiplyStrings(self,s1,s2):
        # code here
        # return the product string
        num = 0
        sign1 = 1
        if s1[0] == '-':
            sign1 = -1
            for i in range(1, len(s1)):
                num = num * 10 + int(s1[i])
        else:
            for i in range(len(s1)):
                num = num * 10 + int(s1[i])
        num = num * sign1

        num2 = 0
        sign2 = 1
        if s2[0] == '-':
            sign2 = -1
            for i in range(1, len(s2)):
                num2 = num2 * 10 + int(s2[i])
        else:
            for i in range(len(s2)):
                num2 = num2 * 10 + int(s2[i])
        num2 = num2 * sign2

        ans = num * num2
        res = ""
        sn = sign1 * sign2
        if sn == 1:
            while ans > 0:
                res = chr((ans % 10) + ord('0')) + res
                ans = ans // 10
        elif sn < 0:
            ans = ans * (-1)
            while ans > 0:
                res = chr((ans % 10) + ord('0')) + res
                ans = ans // 10
            res = '-' + res
        return res



//User function Template for Java

class Solution
{
    public String multiplyStrings(String s1,String s2)
    {
        //code here.
        int sign1=1;
        int sign2=1;
        if(s1.charAt(0)=='-')
        {
            s1=s1.substring(1);
            sign1=-1;
        }
        if(s2.charAt(0)=='-')
        {
            s2=s2.substring(1);
            sign2=-1;
        }
        int n1 = s1.length();
        int n2 = s2.length();
        int[] result = new int[n1 + n2];
        for (int i = n1 - 1; i >= 0; i--) 
        {
            for (int j = n2 - 1; j >= 0; j--) 
            {
                int digit1 = s1.charAt(i) - '0';
                int digit2 = s2.charAt(j) - '0';
                int product = digit1 * digit2;
                int sum = product + result[i + j + 1];
                result[i + j + 1] = sum % 10;
                result[i + j] += sum / 10;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int num : result) 
        {
            if ((sb.length() == 0 && num == 0)) 
            {
            }
            else
            {
                sb.append(num);
            }
        }
        int resultSign = sign1 * sign2;
        if (sb.length() == 0) 
        {
            return "0";
        } 
        else if (resultSign == -1) 
        {
            sb.insert(0, '-');
        }
        return sb.toString();
    }
}
