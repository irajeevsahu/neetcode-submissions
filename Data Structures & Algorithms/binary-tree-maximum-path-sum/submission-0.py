# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val

        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)
            ans = max(ans, node.val + leftMax + rightMax)
            return node.val + max(rightMax, leftMax)

        dfs(root)
        return ans
