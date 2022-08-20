# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        root.parent = None
        def go(node):
            if not node.left and not node.right:
                q.append(node)
            if node.left:
                node.left.parent = node
                go(node.left)
            if node.right:
                node.right.parent = node
                go(node.right)
        
        go(root)
        ans = []
        seen = set()
        while q:
            tmp = []
            tmp_ans = []
            tmp_seen = set()
            tmp_set = set()
            while q:
                node = q.pop()
                #print(node.val, ans, [x.val for x in seen])
                leaf = True
                if (node.left and node.left not in seen) or (node.right and node.right not in seen):
                    leaf = False
                if leaf:
                    tmp_ans.append(node.val)
                    tmp_seen.add(node)
                    if node.parent is not None and node.parent not in tmp_set:
                        tmp.append(node.parent)
                        tmp_set.add(node.parent)
                elif node not in tmp_set:
                    tmp.append(node)
                    tmp_set.add(node)
            q = tmp
            seen |= tmp_seen
            ans.append(tmp_ans)
            
        return ans