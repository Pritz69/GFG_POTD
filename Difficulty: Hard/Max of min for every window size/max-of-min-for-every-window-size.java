class Solution {
   public ArrayList<Integer> maxOfMins(int[] arr) {
        // code here
      
        int n = arr.length;   
        int[] left = new int[n];   
        int[] right = new int[n];  
        int[] ans = new int[n + 1]; 

        
        Stack<Integer> st = new Stack<>();
        for (int i = 0; i < n; i++) {
            while (!st.isEmpty() && arr[st.peek()] >= arr[i]) {
                st.pop();
            }
            left[i] = st.isEmpty() ? -1 : st.peek();
            st.push(i);
        }

        
        st.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!st.isEmpty() && arr[st.peek()] >= arr[i]) {
                st.pop();
            }
            right[i] = st.isEmpty() ? n : st.peek();
            st.push(i);
        }

 
        for (int i = 0; i < n; i++) {
            int len = right[i] - left[i] - 1;
            ans[len] = Math.max(ans[len], arr[i]);
        }

        for (int i = n - 1; i >= 1; i--) {
            ans[i] = Math.max(ans[i], ans[i + 1]);
        }
        ArrayList<Integer> res = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            res.add(ans[i]);
        }
        return res;
    }
}