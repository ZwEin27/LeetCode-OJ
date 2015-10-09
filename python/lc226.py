# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root != None:
            left = None;
            right = None;
            if root.right != None:
                left = self.invertTree(root.right);
            if root.left != None:
                right = self.invertTree(root.left);
            root.left = left;
            root.right = right;

        return root;