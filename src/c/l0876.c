/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* middleNode(struct ListNode* head){
    struct ListNode* fast = head;
    struct ListNode* slow = head;
    while (fast != NULL) {
        fast = fast -> next;
        slow = slow -> next;
        if (fast == NULL) {
            break;
        }
        else {
            fast = fast -> next;
        }
    }
    return slow;
}