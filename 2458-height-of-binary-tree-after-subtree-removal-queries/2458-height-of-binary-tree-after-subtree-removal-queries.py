class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)
    
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        d = defaultdict(tuple); dleft = defaultdict(int); dright = defaultdict(int)
        # inorder traversal
        nodes = []
        def go(node, level):
            min_idx = len(nodes)
            if node.left:
                go(node.left, level+1)
            nodes.append(level)
            if node.right:
                go(node.right, level+1)
            max_idx = len(nodes)-1
            d[node.val] = (min_idx, max_idx)
        
        go(root, 0)
        rq = SegmentTree(nodes)
        ans = []
        N = len(nodes)
        for q in queries:
            l = rq.query(0, d[q][0])
            if d[q][1] + 1 < N:
                r = rq.query(d[q][1]+1, N)
            else:
                r = 0
            if l > r:
                ans.append(l)
            else:
                ans.append(r)
        return ans
            
            