class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> perms, ans;
        string t1(n, '(');
        string t2(n, ')');
        string t = t1 + t2;
        do {
            perms.push_back(t);
        }
        while (next_permutation(t.begin(), t.end()));
        
        for (auto &p: perms) {
            int open = 0;
            int good = 1;
            for (auto &x: p) {
                if (x=='(') {
                    open++;
                }
                else if (x==')' && open>0) {
                    open--;
                }
                else {
                    good = 0;
                }
            }
            if (good) {
                ans.push_back(p);
            }
        }
        
        return ans;
        
    }
};