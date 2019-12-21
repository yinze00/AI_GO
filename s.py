from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        minnode = root
        stack = []
        while minnode.left:
            stack.append(minnode)
            minnode = minnode.left
            int k = 10 