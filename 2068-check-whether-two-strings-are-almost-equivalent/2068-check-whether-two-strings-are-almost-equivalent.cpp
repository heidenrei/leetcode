class Solution {
public:
    bool checkAlmostEquivalent(string word1, string word2) {
        int N;
        N = word1.length();
        int c1[26] = {};
        int c2[26] = {};
        string s = "qwertyuiopasdfghjklzxcvbnm";
        
        for (auto &x: word1) {
            c1[x-'a']++;
        }
        for (auto &x: word2) {
            c2[x-'a']++;
        }
        
        for (auto &x: s) {
            if (abs(c1[x-'a'] - c2[x-'a']) > 3) {
                return false;
            }
        }
        
        return true;
    }
};