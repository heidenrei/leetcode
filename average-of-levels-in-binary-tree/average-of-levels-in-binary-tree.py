# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        if not root:
            return ans
        #bfs
        curr = [root]
        while curr:
            tmp = []
            tmp_N = 0
            tmp_vals = []
            while curr:
                node = curr.pop()
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
                tmp_N += 1
                tmp_vals.append(node.val)
            if tmp_N:
                avg = sum(tmp_vals)/tmp_N
                ans.append(avg)
            curr.extend(tmp)
        return ans