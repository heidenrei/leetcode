class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        people = set()
        balances = [0 for x in range(12)] # + means they are owed money
        for x, y, z in transactions:
            people.add(x)
            people.add(y)
            balances[y] -= z
            balances[x] += z
        tpeople = set()
        for x in people:
            if balances[x] != 0:
                tpeople.add(x)
                
        people = tpeople
        to_rem = set()
        ans = 0
        for x, y in combinations(people, 2):
            if x not in to_rem and y not in to_rem:
                if balances[x] + balances[y] == 0:
                    to_rem.add(x)
                    to_rem.add(y)
                    ans += 1
        
        people ^= to_rem
        
        N = len(people)
        def go(i, debts):
            #print(i, debts)
            if i == N:
                return 0
            if debts[perm[i]] > 0: # current person is owed money
                return inf
            if not debts[perm[i]]:
                return go(i+1, debts)
            ni = i + 1
            while ni < N and not debts[perm[ni]]:
                ni += 1
            
            debts[perm[ni]] += debts[perm[i]]
            debts[perm[i]] = 0
            return go(ni, debts) + 1
        
        
        best = N
        for perm in permutations(people):
        #for perm in [[1,2,0]]:
            #print(perm)
            debts = [x for x in balances]
            tmp = go(0, debts)
            if tmp < best:
                best = tmp
                
        return best + ans
            