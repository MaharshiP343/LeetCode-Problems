class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def chk(r) :

            if not (r):
                return 0

            return max(chk(r.left),chk(r.right)) +1
        
        n = chk (root)

        return n