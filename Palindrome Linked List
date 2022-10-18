# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        node = head
        leng = 0
        comp = []
        while node:
            comp.append(node.val)
            node = node.next
            leng += 1

        for i in range(leng // 2):
            if not comp[i] == comp[len(comp)-i-1]:
                return False
        
        return True 
