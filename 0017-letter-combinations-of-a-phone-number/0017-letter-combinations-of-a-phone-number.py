class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        d = {2: 'abc', 3: 'def', 4: 'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        
        combos = [x for x in d[int(digits[0])]]
        for num in digits[1:]:
            tmp = []
            for char in d[int(num)]:
                for c in combos:
                    tmp.append(c + char)
            combos = tmp
                    
        return combos