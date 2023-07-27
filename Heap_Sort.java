class Solution
{
  
    //Function to build a Heap from array.
    void buildHeap(int arr[], int n)
    {
        // Your code here
        // to get parent for a node 'i' we use (i-1)/2. So, we need to get the parent of the last node in the array,
        // as we need to reach in the 2nd last level of the tree...and start heapifying the tree from the rightmost 
        // node in the 2nd last level. 
        // So parent of last node (rightmost node in the 2nd last level) is = (n-1-1)/2 , Since,last node (i)= n-1 over here.
        // We heapify for each node from 2nd last level, as last level already heapified.
      
        for(int i= (n-1-1)/2 ; i>=0; i--){
            heapify(arr, n, i);
        }
    }
 
    //Heapify function to maintain heap property.
    void heapify(int arr[], int n, int i)
    {
        // Your code here
        int largest=i;
        int l=2*i+1;
        int r=2*i+2;
        if(l<n && arr[l]>arr[largest]){
            largest=l;
        }
        
         if(r<n && arr[r]>arr[largest]){
            largest=r;
        }
        if(largest !=i){
           int temp=arr[i];
           arr[i]=arr[largest];
           arr[largest]=temp;
           heapify(arr, n, largest);
        }
    }
    
    //Function to sort an array using Heap Sort.
    public void heapSort(int arr[], int n)
    {
        //code here
        buildHeap(arr, n);
        for(int i=n-1; i>0; i--){
          int temp= arr[0];
          arr[0]=arr[i];
          arr[i]=temp;
          heapify(arr, i, 0);
        }
    }
 }
 
