class Solution{
    //Function to find the leaders in the array.
    static ArrayList<Integer> leaders(int arr[], int n){
        // Your code here
        ArrayList<Integer> leaders = new ArrayList<>();
        int maxRight = Integer.MIN_VALUE;
        
        for (int i = arr.length - 1; i >= 0; i--) 
        {
            if (arr[i] >= maxRight) 
            {
                maxRight = arr[i];
                leaders.add(maxRight);
            }
        }
        Collections.reverse(leaders);
        return leaders;
    }
}
