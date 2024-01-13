//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;

/* Link list node */
struct Node {
	int data;
	struct Node *next;
	Node(int x) {
		data = x;
		next = NULL;
	}
};

/* Function to print linked list */
void printList(struct Node *head)
{
	struct Node *temp = head;
	while (temp != NULL)
	{
		printf("%d ", temp->data);
		temp = temp->next;
	}
}




// } Driver Code Ends
//User function Template for C++

/*Link list node
struct Node {
	int data;
	struct Node *next;
	Node(int x) {
		data = x;
		next = NULL;
	}
};*/
class Solution
{
    public:
    Node* insertionSort(struct Node* head)
    {
        //code here
        Node* curr = head;
        Node* prev = nullptr;
        while(curr){
            if(prev && prev->data > curr->data)
            {
                Node* temp = head;
                while(temp != curr)
                {
                    if(temp->data > curr->data)
                    {
                        int val = temp->data;
                        temp->data = curr->data;
                        curr->data = val;
                    }
                    temp = temp->next;
                }
            }
            prev = curr;
            curr = curr->next;
        }
        return head;
    }
};

//{ Driver Code Starts.
int main()
{
	int T;
	cin >> T;

	while (T--)
	{
		int n;
		cin >> n;

		Node *head = NULL;
		Node *temp = head;

		for (int i = 0; i < n; i++) {
			int data;
			cin >> data;
			if (head == NULL)
				head = temp = new Node(data);
			else
			{
				temp->next = new Node(data);
				temp = temp->next;
			}
		}

        Solution ob;

		head = ob.insertionSort(head);
		printList(head);

		cout << "\n";



	}
	return 0;
}
// } Driver Code Ends