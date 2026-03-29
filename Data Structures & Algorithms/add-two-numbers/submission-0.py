# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        r_num_1 = ''
        r_num_2 = ''

        curr_1 = l1
        curr_2 = l2

        while curr_1:
            r_num_1 += str(curr_1.val)
            curr_1 = curr_1.next

        while curr_2:
            r_num_2 += str(curr_2.val)
            curr_2 = curr_2.next

        num_1 = r_num_1[::-1]
        num_2 = r_num_2[::-1]

        num_3 = str(int(num_1) + int(num_2))
        r_num_3 = num_3[::-1]

        res = ListNode()
        curr = res

        for i in range(len(r_num_3)):
            curr.val = int(r_num_3[i])
            if i != len(r_num_3) - 1:
                curr.next = ListNode()
                curr = curr.next

        return res

        