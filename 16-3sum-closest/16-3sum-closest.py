class Solution:
    def threeSumClosest(self, nums, target):
        nums = list(sorted(nums))
        out = float('inf')
        i = 0
        j = 0
        k = len(nums)-1
        
        # [-4, -1, 1, 2]
        
        while i < (k-1):
            j = i+1
            k = len(nums)-1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if abs(target-out) > abs(target-tmp):
                    out = tmp
                #print(nums[i], nums[j], nums[k])
                if tmp < target: # need to make nums bigger -> move j to the right
                    j += 1
                elif tmp > target:
                    k -= 1
                else:
                    return tmp
            i += 1
            
        return out