# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []

        def dfs(node):
            if not node:
                return
            ans.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        ans.sort()
        return ans[k - 1]
