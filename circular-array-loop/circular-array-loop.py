class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 1:
            return False
        for i in range(N):
            seen = set()
            def go(idx, og):
                if nums[idx] * nums[og] < 0:
                    return False

                if nums[og] < 0:
                    if idx + nums[idx] < 0:
                        nxt = N - (abs(idx + nums[idx]) % N)
                    else:
                        nxt = idx + nums[idx]

                else:
                    nxt = (idx + nums[idx]) % N
                if nxt == idx:
                    return False
                if nxt in seen:
                    return True

                seen.add(nxt)
                return go(nxt, og)
            if go(i, i):
                return True
            
        return False
        