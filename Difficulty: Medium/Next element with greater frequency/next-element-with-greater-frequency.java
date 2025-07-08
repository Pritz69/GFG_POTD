class Solution {
    public ArrayList<Integer> findGreater(int[] arr) {
        // code here
        ArrayList<Integer> res = new ArrayList<>(); 
        

        HashMap<Integer,Integer> hm = new HashMap<>();
        Stack<Integer> stack = new Stack<>(); 
        
        for (int nums : arr) {
            hm.put(nums, hm.getOrDefault(nums, 0) + 1);
        }
        
        for(int i=0;i<arr.length;i++){
            res.add(-1); 
        }
        
        for(int i=0;i<arr.length;i++)
        {
            while (!stack.isEmpty() && hm.get(arr[stack.peek()]) < hm.get(arr[i])) 
            {
                res.set(stack.pop(), arr[i]);
            }
            stack.push(i);
        }
        
        return res;
        
    }
}

