"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        curr = head
        dummy = new = Node(0) 
        mp = {}
        while curr:
            new.next = Node(curr.val)
            new = new.next
            mp[curr] = new
            curr = curr.next
        curr=head
        while curr:
            new=mp[curr]
            new.random=mp.get(curr.random)
            curr=curr.next
        return dummy.next