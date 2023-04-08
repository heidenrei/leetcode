"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':        
        if not node:
            return None
        cache = {}
        
        def go(node):
            if node in cache:
                return cache[node]
            
            new_node = Node(node.val)
            cache[node] = new_node
            
            for n in node.neighbors:
                new_node.neighbors.append(go(n))
                
            return cache[node]
        return go(node)