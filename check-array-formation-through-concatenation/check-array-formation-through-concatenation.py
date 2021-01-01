class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        N = len(pieces)
        idx = 0
        ans = []
        
        while idx < len(arr):
            added = False
            for i in range(N):
                if arr[idx] == pieces[i][0] and idx + len(pieces[i]) <= len(arr):
                    for j in range(len(pieces[i])):
                        if pieces[i][j] != arr[idx+j]:
                            return False
                    ans.append(pieces)
                    idx += len(pieces[i])
                    added = True
                    break
            if not added:
                idx += 1
        return len(ans) == N
