class Solution
{
    boolean[] prime = new boolean[10000];
    Solution()
    {
        Arrays.fill(prime,true);
        for(int i = 2;i*i<10000;i++){
            if(prime[i]==true){
                for(int j = i*i;j<10000;j+=i){
                    prime[j] = false;
                }
            }
        }
    }
    
    public int shortestPath(int Num1,int Num2){
        // Complete this function using prime array
        
        boolean[]vis=new boolean[10000];
        Queue<int[]> q=new LinkedList<>();
        q.add(new int[]{Num1,0});
        vis[Num1]=true;
        while(!q.isEmpty()){
            int[] curr=q.remove();
            if(curr[0]==Num2)return curr[1];
            
            char[] arr= Integer.toString(curr[0]).toCharArray();
            for(int i=0;i<4;i++){
                for(char ch='0';ch<='9';ch++){
                    char prevChar = arr[i];
                    arr[i]=ch;
                    int newNum = Integer.parseInt(new String(arr));
                    if(!vis[newNum] && prime[newNum] && newNum>=1000){
                        vis[newNum]=true;
                        q.add(new int[]{newNum,curr[1]+1});
                    }
                    arr[i]=prevChar;
                }
            }
        }
        return -1;
    }
}
