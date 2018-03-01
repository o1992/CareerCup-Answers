import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self ,head):
        self.head = head
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self):
        current, length = self.head, 0
        while current is not None:
            current, length = current.next, length + 1

        return self.sortedListToBSTRecu(0, length)

    def sortedListToBSTRecu(self, start, end):
        if (start == end):
            return None
        mid = math.floor(start + (end - start) / 2)
        left = self.sortedListToBSTRecu(start, mid)
        current = TreeNode(self.head.val)
        current.left = left
        self.head = self.head.next
        current.right = self.sortedListToBSTRecu(mid + 1, end)
        return current


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
result = Solution(head)
val = result.sortedListToBST()
print(val.val)
print(val.left.val)
print(val.left.left.val)
print(val.right.val)