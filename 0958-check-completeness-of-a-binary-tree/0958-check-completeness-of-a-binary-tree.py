# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        while q:
            tmp = []
            ncnt = 0
            while q:
                x = q.pop()
                if x is None:
                    continue
                if x.left:
                    tmp.append(x.left)
                else:
                    tmp.append(None)
                    ncnt += 1
                if x.right:
                    tmp.append(x.right)
                else:
                    tmp.append(None)
                    ncnt += 1
            
            if ncnt:
                # need to make sure Nones are all at right of list
                has_none = False
                for x in tmp:
                    if x is None:
                        has_none = True
                    else:
                        if has_none:
                            return False
                # need to make sure they're all leaves
                for x in tmp:
                    if x and (x.left or x.right):
                        return False
                return True
            elif tmp:
                q = tmp[::-1]
            else:
                return True
                
            