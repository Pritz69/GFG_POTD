class Solution {
  public:
    int minLaptops(int n, int start[], int end[]) {

        sort(start,start+n);

        sort(end,end+n);

        int laptopCount=1, i=1, j=0;

        while(i<n && j<n){

            if(start[i]<end[j]) laptopCount++;

            else j++;

            i++;

        }

        return laptopCount;

    }
};
