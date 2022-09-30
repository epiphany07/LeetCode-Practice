/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* createNode(){
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
    node->next = NULL;
    return node;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    
    struct ListNode *head, *temp = NULL;
    temp = head = createNode();
    int c = 0, sum;

    while (l1 || l2) {
        sum = c;
        temp->next = createNode();
        temp = temp->next;
        
        if(l1){
            sum+= l1->val;
            l1 = l1->next;
        }
        if(l2){
            sum+= l2->val;
            l2 = l2 ->next;
        }
        
        temp->val = sum % 10;
        c = sum / 10;
    }

    if (c) {
        temp->next = createNode();
        temp->next->val = c;
    }
    return head->next;
 
}