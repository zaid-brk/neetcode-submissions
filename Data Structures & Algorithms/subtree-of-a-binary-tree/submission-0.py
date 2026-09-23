# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            if a.val != b.val:
                return False

            return same_tree(a.left, b.left) and same_tree(a.right, b.right)


        def search_node(node):
            if node is None:
                return False

            if same_tree(node, subRoot):
                return True

            return search_node(node.left) or search_node(node.right)


        return search_node(root)
        