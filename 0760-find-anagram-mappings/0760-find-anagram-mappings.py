class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d2 = defaultdict(list)
        for i, x in enumerate(nums2):
            d2[x].append(i)
        ans = []
        for x in nums1:
            ans.append(d2[x].pop())
        return ans