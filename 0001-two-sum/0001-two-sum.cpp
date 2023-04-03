class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int k) {
        map<int, int> d;
        vector<int> ans(2, 0);

        int n = nums.size();
        for (int i=0;i<n;i++) {
            if (d.find(nums[i]) != d.end()) {
                ans[0] = i;
                ans[1] = d[nums[i]];
            }
            else {
                d[k-nums[i]] = i;
            }
        }
        return ans;
    }
};