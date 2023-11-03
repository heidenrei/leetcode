class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        if not target:
            return []
        
        if not n:
            return []
        
        res = []
        arr = []
        for num in range(1, n+1):
            if arr == target:
                return res
            else:
                if num in target:
                    arr.append(num)
                    res.append('Push')
                else:
                    arr.append(num)
                    res.append('Push')

                    arr.pop()
                    res.append('Pop')
                    
        return res