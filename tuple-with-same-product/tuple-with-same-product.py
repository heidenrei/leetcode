class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        N = len(nums)
        products = defaultdict(list)
        cnt = 0
        nums.sort()
        for i in range(N):
            for j in range(i):
                if nums[i] != nums[j]:
                    products[nums[i]*nums[j]].append([i, j])
        
        seen = set()
        
        for i in range(N):
            for j in range(i):
                if nums[i] * nums[j] in products:
                    for x, y in products[nums[i]*nums[j]]:
                        if i != x and j != x and y != j and y != i:
                            cnt += 4
        return cnt
