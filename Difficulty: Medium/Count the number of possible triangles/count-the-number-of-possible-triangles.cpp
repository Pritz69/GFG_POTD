class Solution {
  public:
    int countTriangles(vector<int>& arr) {
    int n = arr.size();
    sort(arr.begin(), arr.end());
    int count = 0;

    for (int k = n - 1; k >= 2; k--) {
        int i = 0, j = k - 1;
        while (i < j) {
            if (arr[i] + arr[j] > arr[k]) {
                count += (j - i); // all elements between i and j are valid
                j--;
            } else {
                i++;
            }
        }
    }
    return count;
    }
};
