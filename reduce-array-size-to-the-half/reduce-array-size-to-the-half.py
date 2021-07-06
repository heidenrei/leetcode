class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        N = len(arr)
        t = N // 2 
        c = Counter(arr)
        
        nums = [v for k, v in c.items()]
        nums.sort(reverse=True)
        i = 0
        while N > t:
            N -= nums[i]
            i += 1
        return i