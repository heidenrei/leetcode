class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max = 0;
            for (int i = 0; i < nums.size(); i++) {
                for (int j = 0; j < i; j ++) {
                    if (((nums[i] - 1)*(nums[j]-1)) > max) {
                        max = ((nums[i] - 1)*(nums[j]-1));
                    }
                }
            }
        return max;
    }
};
