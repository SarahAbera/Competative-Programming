# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head   
        lst = head  
        while(lst.next!=None):
            if lst.val == lst.next.val:
                lst.next = lst.next.next
            else:
                lst = lst.next 
        return head 
