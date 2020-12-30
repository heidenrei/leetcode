class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return [x[1] for x in paths if x[1] not in set([x[0] for x in paths])][0]
