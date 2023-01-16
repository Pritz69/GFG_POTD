    public static long[] nextLargerElement(long[] arr, int n)
    { 
        // Your code here
        long[]a=new long[n];
        for(int i=0;i<n;i++) {
            a[i]=-1;
        }
        Stack<Integer> st=new Stack<>();
        st.push(0);
        for(int i=1;i<n;i++) {
            if(arr[i]<=arr[st.peek()]) {
                st.push(i);
            }
            else {
                while(st.size()!=0 && arr[i]>arr[st.peek()]) {
                    int x=st.peek();
                    a[x]=arr[i];
                    st.pop();
                }
                st.push(i);
            }
        }
        return a;
    }
