# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        self.idx = 0
        
        def build(min_val, max_val):
            if self.idx >= len(preorder):
                return None
            
            val = preorder[self.idx]
            if val < min_val or val > max_val:
                return None
            
            node = TreeNode(val)
            self.idx += 1
            node.left = build(min_val, val)
            node.right = build(val, max_val)
            
            return node
        
        return build(float('-inf'), float('inf'))