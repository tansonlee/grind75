'''
Solution 1:
let n = depth of p
let m = depth of q
Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))
'''
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    visited = set()

    # find p
    currp = root
    visited.add(currp.val)
    while not (currp.val == p.val):
        if (currp.val < p.val):
            currp = currp.right
        else:
            currp = currp.left
        visited.add(currp.val)

    # find q
    currq = root;
    path = deque();
    path.append(currq)
    while not (currq.val == q.val):
        if (currq.val < q.val):
            currq = currq.right
        else:
            currq = currq.left
        path.append(currq)

    while (len(path) > 0):
        c = path.pop()
        if c.val in visited:
            return c

'''
Solution 2:
Time Complexity: O(max(n, m))
Space Complexity: O(1)
'''
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    lower = p if p.val < q.val else q
    higher = p if p.val >= q.val else q
    if root.val >= lower.val and root.val <= higher.val:
        return root
    if root.val <= lower.val and root.val <= higher.val:
        return self.lowestCommonAncestor(root.right, p, q)
    return self.lowestCommonAncestor(root.left, p, q)
