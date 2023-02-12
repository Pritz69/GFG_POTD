//User function Template for C++

/*

class Node{
public:
    int val;
    Node *next;
    Node(int num){
        val=num;
        next=NULL;
    }
};

*/

class Solution{
bool isprime(int n){

        if (n == 1)

            return false;

        if (n == 2 || n == 3)

            return true;

        if (n % 2 == 0 || n % 3 == 0)

            return false;

        for (int i = 5; i <= sqrt(n); i += 6)

        {

            if (n % i == 0 || n % (i + 2) == 0)

                return false;

        }

        return true;

    }

    int prime(int n){

        int m=n;

        int p=n;

        int j=0, i=0;

        if(n==1){

            return 2;

        }

        while(!isprime(m)){

            m--;

            i++;

        }

        while(!isprime(p)){

            p++;

            j++;

        }

        if(i>j){

            return p;

        }

        else{

            return m;

        }

    }

public:

    Node *primeList(Node *head){

        Node* a=head;

        while(a){

            if(!isprime(a->val)){

                a->val=prime(a->val);

            }

            a=a->next;

        }

        return head;

    }
