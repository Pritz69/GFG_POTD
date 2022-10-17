class Solution{
public:
    ListNode *moveToFront(ListNode *head){
        ListNode *cur = head;
        if(head->next == nullptr)
            return head;
        while(head->next->next !=  nullptr) {
            head = head->next; }
        ListNode *temp = head->next;
        head->next = nullptr;
        temp->next = cur;
        return temp;   
    }   };
