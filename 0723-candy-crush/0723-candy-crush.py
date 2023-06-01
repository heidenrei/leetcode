class Solution:
    def candyCrush(self, A):
        R, C = len(A), len(A[0])
        while 1:
            to_del = []
            for i in range(R):
                curr = A[i][0]
                run = 1
                tmp_del = [[i, 0]]
                for j in range(1, C):
                    if A[i][j] == curr:
                        run += 1
                        tmp_del.append([i, j])
                    else:
                        if run >= 3 and curr:
                            to_del.extend(tmp_del)
                        run = 1
                        curr = A[i][j]
                        tmp_del = [[i, j]]
                if run >= 3 and curr:
                    to_del.extend(tmp_del)
            for j in range(C):
                curr = A[0][j]
                run = 1
                tmp_del = [[0, j]]
                for i in range(1, R):
                    if A[i][j] == curr:
                        run += 1
                        tmp_del.append([i, j])
                    else:
                        if run >= 3 and curr:
                            to_del.extend(tmp_del)
                        run = 1
                        curr = A[i][j]
                        tmp_del = [[i, j]]
                if run >= 3 and curr:
                    to_del.extend(tmp_del)
            if not to_del:
                for x in A:
                    print(x)
                return A
            else:
                for i, j in to_del:
                    A[i][j] = 0
                for j in range(C):
                    for i in range(R-1)[::-1]:
                        if not A[i+1][j] and A[i][j]:
                            ti = i
                            while ti < R-1 and not A[ti+1][j]:
                                A[ti][j], A[ti+1][j] = A[ti+1][j], A[ti][j]
                                #print('1111')
                                ti += 1
                                