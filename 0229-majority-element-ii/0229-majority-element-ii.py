class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        e1, e2, c1, c2 = None, None, 0, 0
        for x in nums:
            if x == e1:
                c1 += 1
            elif x == e2:
                c2 += 1
            elif c1 == 0:
                e1, c1 = x, 1
            elif c2 == 0:
                e2, c2 = x, 1
            else:
                c1, c2 = c1 - 1, c2 - 1
       # print(e1, e2)
        return [x for x in [e1, e2] if nums.count(x) > len(nums)//3]