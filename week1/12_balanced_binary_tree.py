'''
Solution 1:
let n = number of nodes
Time complexity: O(n)
Space complexity: O(n)
'''
def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, height = self.balancedAndHeight(root)
        return balanced
    
    def balancedAndHeight(self, root):
        if root is None:
            return (True, 0)
        
        left_balanced, left_height = self.balancedAndHeight(root.left)
        right_balanced, right_height = self.balancedAndHeight(root.right)
        
        if not left_balanced or not right_balanced:
            return (False, max(left_height, right_height) + 1)
        
        if abs(left_height - right_height) <= 1:
            return (True, max(left_height, right_height) + 1)
        
        return (False, max(left_height, right_height)  + 1)





