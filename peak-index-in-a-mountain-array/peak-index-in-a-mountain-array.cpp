class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int best = 0;
        int ans = 0;
        for (int i = 1; i < arr.size()-1; i++) {
            if (arr[i] > best) {
                best = arr[i];
                ans = i;
            }
        }
        return ans;
    }
};
