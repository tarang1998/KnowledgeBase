//https://leetcode.com/problems/middle-of-the-linked-list/

class Solution{
    public: 
        //Time Complexity : O(n)
        //Space Complexity : O(1)
        ListNode* middleNode(ListNode* head){

            int n = 0;
            ListNode* temp = head;

            while(temp){
                n++;
                temp = temp->next;
            }

            temp = head;


            for(int i=0; i<n/2;i++){
                temp = temp->next;
            }

            return temp;
        }

        ListNode* middleNode2(ListNode* head){

            ListNode* slow = head;
            ListNode* fast = head;

            while(fast && fast->next){
                slow = slow->next;
                fast = fast->next->next;
            };

            return slow;
        }
};