class Solution {
public:
    int smallestValue(int n) {
        unordered_set<int> primes = {2};
        unordered_set<int> comps;
        
        for (int x=3;x<=n;x+=2){
            if (comps.find(x)==comps.end()){
                primes.insert(x);
                int tx = x*2;
                while (tx<=n) {
                    comps.insert(tx);
                    tx += x;
                }
            }
        }
        unordered_set<int> seen;
        while (1){
            int tmpn = 0;
            for (auto &x: primes) {
                while (n%x==0) {
                    tmpn += x;
                    n = n/x;
                }
            }
            n = tmpn;
            if (seen.find(n) != seen.end()){
                return n;
            }
            else {
                seen.insert(n);
            }
        }
        return 0;
    }
};