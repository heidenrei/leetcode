class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& A) {
        int N = A.size();
        sort(A.begin(), A.end());
        vector<int> dp(N, 1);;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (A[i][0] > A[j][0] && A[i][1] > A[j][1] && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                }
            }
        }
        int ans = 1;
        for (int i = 0; i < N; i++) {
            if (dp[i] > ans) {
                ans = dp[i];
            }
        }
        return ans;
    }
};