from sortedcontainers import SortedList

class Solution:
    def getBiggestThree(self, A):
        R, C = len(A), len(A[0])
        # 50**4.. 6M
        sl = SortedList(key=lambda x: -x)
        for j in range(C):
            for i1 in range(R):
                for i2 in range(i1+1):
                    d = i1 - i2
                    mid_i = i1 - d//2
                    left_j = j - d//2
                    right_j = j + d//2
                    good = False
                    if left_j >= 0 and right_j < C and d % 2 == 0:
                        good = True
                    if not good:
                        continue
                    # print('left', mid_i, left_j)
                    # print('top', i2, j)
                    # print('right', mid_i, right_j)
                    # print('bot', i1, j)
                    tmp = 0
                    ni, nj = mid_i, left_j
                    for di in range(d//2):
                        ni, nj = ni - 1, nj + 1
                        tmp += A[ni][nj]
                    ni, nj = i2, j
                    for di in range(d//2):
                        ni, nj = ni + 1, nj + 1
                        #print(ni, nj)
                        tmp += A[ni][nj]
                    ni, nj = mid_i, right_j
                    for di in range(d//2):
                        ni, nj = ni + 1, nj - 1
                        tmp += A[ni][nj]
                    ni, nj = i1, j
                    for di in range(d//2):
                        ni, nj = ni - 1, nj - 1
                        tmp += A[ni][nj]
                    if right_j == left_j:
                        tmp += A[mid_i][right_j]
                    # print(tmp)
                    # print()
                    if tmp not in sl:
                        sl.add(tmp)
                    if len(sl) > 3:
                        sl.pop()
                
                            
        return sl