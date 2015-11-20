/*
 You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
 */
class Solution {
    public:
    ListNode* addTwoNumbers(ListNode *l1, ListNode *l2) {
        ListNode *output= new ListNode(0);
        ListNode *head= output;
        output->next=NULL;
        int temp=0,carry=0;
        while(l1!=NULL & l2!=NULL){
            temp=l1->val+l2->val+carry;
            if(temp>9){
                carry=temp/10;
                temp=temp%10;
            }
            else{
                carry=0;
            }
            output->next=new ListNode(temp);
            output=output->next;
            l1=l1->next;
            l2=l2->next;
        }
        while(l1!=NULL){
            temp=l1->val+carry;
            if(temp>9){
                carry=temp/10;
                temp=temp%10;
            }
            else{
                carry=0;
            }
            output->next=new ListNode(temp);
            output=output->next;
            l1=l1->next;
        }
        while(l2!=NULL){
            temp=l2->val+carry;
            if(temp>9){
                carry=temp/10;
                temp=temp%10;
            }
            else{
                carry=0;
            }
            output->next=new ListNode(temp);
            output=output->next;
            l2=l2->next;
        }
        if(carry>0){
            output->next=new ListNode(carry);
            output=output->next;
        }
        return head->next;
    }
};