import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9+7
        N = len(nums1)
        best = math.inf
        diffs = []
        
        for i in range(N):
            diffs.append(abs(nums1[i] - nums2[i]))
        
        score = sum(diffs)
        
        nums1_sorted = sorted(list(set(nums1)))
        #print(nums1_sorted)
        # print(N)
        for i in range(N):
            tmp = abs(nums1[i] - nums2[i])
            closest_higher_idx = bisect.bisect_right(nums1_sorted, nums2[i])
            closest_lower_idx = bisect.bisect_left(nums1_sorted, nums2[i])
            
            closest_higher_idx = min(N-1, closest_higher_idx)
            closest_lower_idx = min(N-1, closest_lower_idx)
            
            #print(closest_higher_idx, closest_lower_idx)
            
            if closest_higher_idx + 1 < len(nums1_sorted):
                if abs(nums1_sorted[closest_higher_idx+1]) - nums2[i] < abs(nums1_sorted[closest_lower_idx-1]) - nums2[i]:
                    tmp_diff = abs(nums1_sorted[closest_higher_idx+1] - nums2[i])
                else:
                    if closest_lower_idx > 0:
                        tmp_diff = abs(nums1_sorted[closest_lower_idx-1] - nums2[i])
                    else:
                        tmp_diff = abs(nums1_sorted[0] - nums2[i])
            else:
                if closest_lower_idx > 0:
                    tmp_diff = abs(nums1_sorted[closest_lower_idx-1] - nums2[i])
                else:
                    tmp_diff = abs(nums1_sorted[0] - nums2[i])
            
            if closest_lower_idx < len(nums1_sorted) and abs(nums1_sorted[closest_lower_idx] - nums2[i]) < tmp_diff:
                tmp_diff = abs(nums1_sorted[closest_lower_idx] - nums2[i])
            
            score -= tmp
            score += tmp_diff
            if score < best:
                pass
                #print(i, nums1[i], nums2[i], tmp_diff)
            best = min(score, best)
            score -= tmp_diff
            score += tmp
        
        return best % MOD
    