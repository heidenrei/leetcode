class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        vector<char> ans;
        int n = strs.size();
        int m = 200;
        for (auto &x: strs) {
            m = fmin(m, x.length());
        }
        for (int j=0;j<m;j++){
            bool good = true;
            for (int i=0;i<n;i++){
                if (strs[i][j] != strs[0][j]){
                    good = false;
                    break;
                }
            
            }
            if (!good){
                break;
            }
            else {
                ans.push_back(strs[0][j]);
            }
            
        }
        string ret = {ans.begin(), ans.end()};
        return ret;
    }
};