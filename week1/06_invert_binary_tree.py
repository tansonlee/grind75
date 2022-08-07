'''
Solution 1
let n be the number of nodes in the tree
let h be the height of the tree
Time Complexity: O(n)
Space Complexity: O(h)
'''
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root


'''
Solution 2
Time Complexity: O(n)
Space Complexity: O(n)
'''
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            curr = queue.get()
            if curr is None:
                continue
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            queue.put(curr.left)
            queue.put(curr.right)
        return root