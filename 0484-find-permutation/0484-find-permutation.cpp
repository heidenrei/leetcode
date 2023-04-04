class Solution {
public:
    vector<int> findPermutation(string s) {
        vector<int> ans, stack;
        s.push_back('I');
        int n = s.length();
        for (int i=0;i<n;i++) {
            if (s[i]=='D') {
                stack.push_back(i+1);
            }
            else {
                ans.push_back(i+1);
                while (!stack.empty()) {
                    int u = stack.back();
                    stack.pop_back();
                    ans.push_back(u);
                }
            }
        }
        return ans;
    }
};