class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = [x for x in dominoes]
        q = []
        N = len(dominoes)
        for i in range(N):
            if dominoes[i].isalpha():
                q.append(tuple([i, dominoes[i]]))
        while q:
            tmp = set()
            while q:
                i, DIR = q.pop()

                if DIR == 'L' and i-1 >= 0:
                    if tuple([i-1, 'R']) in tmp:
                        tmp.remove(tuple([i-1, 'R']))
                    else:
                        if not dominoes[i-1].isalpha():
                            tmp.add(tuple([i-1, 'L']))
                elif DIR == 'R' and i + 1 < N:
                    if tuple([i+1, 'L']) in tmp:
                        tmp.remove(tuple([i+1, 'L']))
                    else:
                        if not dominoes[i+1].isalpha():
                            tmp.add(tuple([i+1, 'R']))
            for i, DIR in tmp:
                dominoes[i] = DIR
            q.extend(list(tmp))
            
        return ''.join(dominoes)