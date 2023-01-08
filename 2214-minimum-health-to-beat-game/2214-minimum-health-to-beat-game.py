class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        N = len(damage)
        
        maxi = max(damage)
        for i in range(N):
            if damage[i] == maxi:
                damage[i] = max(0, damage[i] - armor)
                break
        
        pfs = list(accumulate(damage))
        return max(pfs) + 1
        
#         @cache
#         def is_good(i, x):
#             if i == N:
#                 return True
#             if x - damage[i] > 0 and is_good(i+1, x - damage[i]):
#                     return True
#             # elif x - max(0, damage[i] - armor) > 0 and not used:
#             #     if is_good(i+1, x - max(damage[i] - armor, 0), True):
#             #         return True
#             #     else:
#             #         return False
#             else:
#                 return False
        
# #         for x in range(8, 13):
# #             print(x, is_good(0, x, 0))
        
# #         return 0

#         def is_good(x):
            
        
#         l, r = 0, sum(damage)
#         while l <= r:
#             m = l + r >> 1
#             if is_good(0, m):
#                 r = m - 1
#             else:
#                 l = m + 1
                
#         return r + 1