class Node:
    def __init__(self):
        self.children = {}
        self.cnt = 0
        
class Trie:
    def __init__(self):
        self.root = Node()
    
    def cnt_up_to(self, num, lim):
        curr = self.root
        ans = 0
        for i in range(17, -1,-1):
            numBit = 1 & (num>>i)
            limBit = 1 & (lim>>i)
            
            if limBit and numBit:
                if 1 in curr.children:
                    ans += curr.children[1].cnt
                if 0 in curr.children:
                    curr = curr.children[0]
                else:
                    return ans
                
            elif limBit and not numBit:
                if 0 in curr.children:
                    ans += curr.children[0].cnt
                if 1 in curr.children:
                    curr = curr.children[1]
                else:
                    return ans
            elif not limBit and numBit:
                if 1 in curr.children:
                    curr = curr.children[1]
                else:
                    return ans
            else:
                if 0 in curr.children:
                    curr = curr.children[0]
                else:
                    return ans
        ans += curr.cnt
        return ans
                

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        t = Trie()
        ans = 0
        for num in nums:
            ans += t.cnt_up_to(num, high) - t.cnt_up_to(num, low-1)
            
            curr = t.root
            for i in range(17, -1, -1):
                if 1 & (num>>i):
                    if 1 not in curr.children:
                        curr.children[1] = Node()
                    curr.children[1].cnt += 1
                    curr = curr.children[1]
                else:
                    if 0 not in curr.children:
                        curr.children[0] = Node()
                    curr.children[0].cnt += 1
                    curr = curr.children[0]
                    
        return ans