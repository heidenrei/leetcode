class Solution {
public:
    void setZeroes(vector<vector<int>>& A) {
        unordered_set<int> rows;
        unordered_set<int> cols;
        int r = A.size();
        int c = A[0].size();
        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++) {
                if (!A[i][j]){
                    rows.insert(i);
                    cols.insert(j);
                }
            }
        }
        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++) {
                if ((rows.find(i) != rows.end()) | (cols.find(j) != cols.end())) {
                    A[i][j] = 0;
                }
            }
        }
        
    }
};