"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None
        
        q = [root]
        ans = []
        while q:
            tmp = []
            tmp_ans = []
            for x in q:
                tmp_ans.append(x.val)
                for child in x.children:
                    tmp.append(child)
            q = tmp
            if tmp_ans:
                ans.append(tmp_ans)
            
        return ans