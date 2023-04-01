class Solution {
public:
    int makePrefSumNonNegative(vector<int>& nums) {
        int res = 0;
        long long sum = 0;
        multiset<int> nags;
        for (auto x:nums) {
            sum += x;
            
            if (x<0) nags.insert(x);
            while (sum<0) {
                sum -= nags.extract(nags.begin()).value();
                res++;
            }
        }
    return res;
    }
};