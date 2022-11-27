String addBinary(String A, String B) {
        // code here
        int i=A.length()-1,j=B.length()-1;
        int c=0;
        StringBuilder sb = new StringBuilder();
        while(i>=0 && j>=0) {
            int a1 = A.charAt(i)-'0';
            int b1 = B.charAt(j)-'0';
            sb.append((a1^b1^c));
            i--;
            j--;
            c = ((a1&b1) | (b1&c) | (a1&c));
        }
        while(i>=0) {
            int a1 = A.charAt(i)-'0';
            sb.append((a1^c));
            c = a1&c;
            i--;
        }
        
        while(j>=0) {
            int b1 = B.charAt(j)-'0';
            sb.append((b1^c));
            c = b1&c;
            j--;
        }
        
        sb.append(c);
        sb.reverse();
        i=0;
        while(i<sb.length() && sb.charAt(i)=='0') {
            i++;
        }
        sb.delete(0,i);
        return sb.toString();
    }
