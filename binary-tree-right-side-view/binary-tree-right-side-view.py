# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        ans = [root.val]
        q = deque([root])
        
        while q:
            tmp = []
            while q:
                curr = q.popleft()
                if curr.left:
                    tmp.append(curr.left)
                if curr.right:
                    tmp.append(curr.right)
            if tmp:
                ans.append(tmp[-1].val)
            q.extend(tmp)
            
        return ans