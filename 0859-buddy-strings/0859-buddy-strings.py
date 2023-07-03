class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        made_swap = False
        diffss = []
        diffsg = []
        N = len(s)
        if len(goal) != N:
            return False
        for i in range(N):
            if s[i] != goal[i]:
                diffss.append(s[i])
                diffsg.append(goal[i])
        if not diffss:
            return max(Counter([x for x in s]).values()) >= 2
        elif len(diffss) != 2:
            return False
        else:
            return sorted(diffss) == sorted(diffsg)
        