class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        R = len(board)
        DIRS = [[0,1], [1,0], [0,-1],[-1,0]]
        
        letters = 'qwertyuiopasdfghjklzxcvbnm'
        d = defaultdict(str)
        
        for source in letters:
            for dest in letters:
                tmp = ''
                for i in range(R):
                    for j in range(len(board[i])):
                        if source == board[i][j]:
                            source_i, source_j = i, j
                        if dest == board[i][j]:
                            dest_i, dest_j = i, j
                
                if dest == 'z':
                    if dest_j > source_j:
                        tmp += 'R'*(dest_j-source_j)
                    elif source_j > dest_j:
                        tmp += 'L'*(source_j-dest_j)

                    if dest_i > source_i:
                        tmp += 'D'*(dest_i-source_i)
                    elif source_i > dest_i:
                        tmp += 'U'*(source_i-dest_i)
                else:
                    if dest_i > source_i:
                        tmp += 'D'*(dest_i-source_i)
                    elif source_i > dest_i:
                        tmp += 'U'*(source_i-dest_i)
                        
                    if dest_j > source_j:
                        tmp += 'R'*(dest_j-source_j)
                    elif source_j > dest_j:
                        tmp += 'L'*(source_j-dest_j)
                    
                d[tuple([source, dest])] = tmp
                
        ans = ''
        for i in range(len(target)):
            if i == 0:
                ans += d[tuple(['a', target[i]])]
            else:
                ans += d[tuple([target[i-1], target[i]])]
            ans += '!'
            
        return ans
            
        