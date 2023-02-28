"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, A: List[List[int]]) -> 'Node':
        R, C = len(A), len(A[0])
        def go(i, j, ii, jj):
            #print(i, j, ii, jj)
            curr = Node(0, 0, None, None, None, None)
            vals = set()
            for ni in range(i, ii):
                for nj in range(j, jj):
                    vals.add(A[ni][nj])
            if len(vals) == 1:
                curr.isLeaf = True
                if 1 in vals:
                    curr.val = 1
                else:
                    curr.val = 0
                return curr
            
            curr.isLeaf = False
            curr.topLeft = go(i, j, i+ii>>1, j+jj>>1)
            curr.topRight = go(i, j+jj>>1, i+ii>>1, jj)
            curr.bottomLeft = go(i+ii>>1, j, ii, j+jj>>1)
            curr.bottomRight = go(i+ii>>1, j+jj>>1, ii, jj)
            return curr
            
        return go(0,0,R,C)