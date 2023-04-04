class Solution {
public:
    int partitionString(string s) {
        unordered_set<char> curr;
        int ans = 1;
        for (auto &x: s) {
            if (curr.find(x) != curr.end()) {
                ans++;
                curr.clear();
                curr.insert(x);
                
            }
            else {
                curr.insert(x);
            }
        }
        return ans;
    }
};