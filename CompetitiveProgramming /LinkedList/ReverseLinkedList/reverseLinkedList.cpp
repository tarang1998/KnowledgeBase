//https://leetcode.com/problems/reverse-linked-list/

public class ListNode{
    int val 
    ListNode* next;


    ListNode(){}

    ListNode(int val){
        this.val = val;
    }

    ListNode(int val , ListNode* nextNode){
        this.val = val;
        this.next = nextNode;
    }
}


class Solution{

    //Time Complexity : O(n)
    //Space Complexity : O(1)

    public: 

        ListNode* reverseList(ListNode* head){

            ListNode* prevNode = NULL;
            ListNode* currentNode = head;
            ListNode* nextNode;


            while(currentNode){

                nextNode = currentNode->next;
                currentNode->next = prevNode;

                prevNode = currentNode;
                currentNode = nextNode;

            }

            return prevNode;
        }

        ListNode reverseList2(ListNode* head){

                ListNode* updatedHead = NULL;

                while(head){
                    ListNode* next = head->next;
                    head->next = updatedHead;

                    updatedHead = head;
                    head = next;
                }

                return updatedHead;


        }

    
};