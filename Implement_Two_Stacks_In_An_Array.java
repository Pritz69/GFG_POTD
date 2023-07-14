class twoStacks
{
    int arr[];
    int size;
    int top1, top2;
    twoStacks()
    {
        size = 100; 
        arr = new int[100]; 
        top1 = -1; 
        top2 = size;
    }
    //Function to push an integer into the stack1.
    void push1(int x)
    {
        this.top1 +=1;
        this.arr[top1] =x;
    }
    //Function to push an integer into the stack2.
    void push2(int x)
    {
       this.top2 -=1;
       this.arr[top2] =x;
    }
    //Function to remove an element from top of the stack1.
    int pop1()
    {
        if (this.top1==-1)
        {
            return -1;
        }
        int ans=this.arr[this.top1];
        this.arr[this.top1]=0;
        this.top1 -=1;
        return ans;
    }
    //Function to remove an element from top of the stack2.
    int pop2()
    {
        if (this.top2==this.size)
        {
            return -1;
        }
        int ans=this.arr[this.top2];
        this.arr[this.top2]=0;
        this.top2 +=1;
        return ans;
    }
}
