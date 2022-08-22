class Solution:
    def findShortestWay(self, A: List[List[int]], ball: List[int], hole: List[int]) -> str:
        R, C = len(A), len(A[0])
        for i in range(R):
            A[i] = [1] + A[i] + [1]
        tA = [[1]*(C+2)]
        tA.extend(A)
        tA.append([1]*(C+2))
        A = tA
        DIRS = {'u':[-1,0], 'l':[0,-1],'r':[0,1],'d':[1,0]}
        found_ans = False
        best = inf
        best_path = defaultdict(list)
        arrival = defaultdict(lambda: inf)
        @cache
        def go(i, j, d, cost, path):
            #print(i, j, d)
            if arrival[(i, j, d)] < cost:
                return
            else:
                arrival[(i, j, d)] = cost
            if i == hole[0]+1 and j == hole[1]+1:
                #print('found ans ....')
                nonlocal best, best_path
                if cost <= best:
                    best = cost
                    best_path[cost].append(path)
                return

            ni, nj = i + DIRS[d][0], j + DIRS[d][1]
            if A[ni][nj]:
                # stopped... need to amke next move
                for nd in DIRS:
                    ni, nj = i + DIRS[nd][0], j + DIRS[nd][1]
                    if not A[ni][nj]:
                        go(ni, nj, nd, cost+1, path + nd)
            else:
                go(ni, nj, d, cost+1, path)
                    
        for d in DIRS:
            ni, nj = ball[0]+1 + DIRS[d][0], ball[1]+1 + DIRS[d][1]
            if not A[ni][nj]:
                go(ball[0]+1, ball[1]+1, d, 0, d)
        if best == inf:
            return 'impossible'
        best_path[min(best_path.keys())].sort()
        return best_path[min(best_path.keys())][0]
        
            