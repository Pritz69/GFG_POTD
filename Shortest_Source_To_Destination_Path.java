

// User function Template for Java

class Pair
{
        int first;
        int second;
        int third;
        Pair(int d,int a,int b)
        {
            first=d;
            second=a;
            third=b;
        }
}
class Solution {
    int shortestDistance(int N, int M, int A[][], int X, int Y) {
        // code here
        int ti[]={0,0,-1,1};
        int tj[]={-1,1,0,0};
        Queue<Pair> q=new LinkedList<>();
        q.offer(new Pair(0,0,0));
        while (!q.isEmpty())
        {
            Pair temp=q.poll();
            int di=temp.first;
            int x=temp.second;
            int y=temp.third;
            if (x==X && y==Y)
            {
                return di;
            }
            for(int i=0;i<4;i++)
            {
                int ni=x+ti[i];
                int nj=y+tj[i];
                if (ni>=0 && ni<N && nj>=0 && nj<M && A[ni][nj]==1)
                {
                    q.offer(new Pair(di+1,ni,nj));
                    A[ni][nj]=0;
                }
            }
        }
        return -1;
    }
};
