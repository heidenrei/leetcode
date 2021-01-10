class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        M = len(beginWord)
        N = len(wordList)
        d = defaultdict(set)
        
        for word in wordList:
            for k in range(M):
                tmp = word[:k] + '_' + word[k+1:]
                d[tmp].add(word)
        
        q = deque([beginWord])
        seen = set([beginWord])
        level = 0
        while q:
            tmp = []
            while q:
                curr = q.pop()
                if curr == endWord:
                    return level + 1
                else:
                    for i in range(M):
                        nc = curr[:i] + '_' + curr[i+1:]
                        if nc in d:
                            for nc2 in d[nc]:
                                if nc2 not in seen:
                                    seen.add(nc2)
                                    tmp.append(nc2)
            q.extend(tmp)
            level += 1
        return 0
