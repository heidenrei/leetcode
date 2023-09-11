class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        for i, x in enumerate(groupSizes):
            d[x].append(i)
        ans = []
        for k, v in d.items():
            # k is size need v//k lists
            for i in range(0, len(v), k):
                ans.append(v[i:i+k])
        return ans