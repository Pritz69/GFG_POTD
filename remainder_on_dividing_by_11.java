class Solution 
{ 
     static int xmod11(String x)
	{    
	    // code here
    int result = 0; 
    for (int i = 0; i < x.length(); i++) 
    { 
        
        char c = x.charAt(i); 
        
        int digit = c - '0'; 
        
        result = (result * 10 + digit) % 11;
    }

    return result; 
	}
} 
