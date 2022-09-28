/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    int i=2;
    struct ListNode *temp = head;
    int count = 0;
    while(temp != NULL){ 
        count++ ; temp = temp -> next;
    }
    int pos = count-n +2;

    if(head -> next == NULL){
        free(head);

        return NULL;
    }
    else if(n == 1){
        struct ListNode *tempo = head , *prev;
        while(tempo -> next != NULL){
            prev = tempo;
            tempo = tempo -> next;
        }
        prev -> next = NULL;
        free(tempo);
        return head;
    }
    else if(n == count){
        struct ListNode *tempo = head;
        head = head -> next;
        free(tempo);
        return head;

    }

    else{
        struct ListNode *tempo = head , *prev;
        while((i<pos) && tempo -> next != NULL){
            prev = tempo;
            tempo = tempo -> next;
            i++;
        }
        prev -> next = tempo -> next;
        free(tempo);
        return head;
    }
    return head;

}