class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        d = defaultdict(set)
        
        maps = defaultdict(list)
        
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                maps[word[:i] + '!' + word[i+1:]].append(word)
                
        for k, v in maps.items():
            for i in range(len(v)):
                for j in range(i):
                    d[v[i]].add(v[j])
                    d[v[j]].add(v[i])
                
        seen = set([beginWord])
        q = [[beginWord]]
        while q:
            tmp = []
            curr_ans = []
            while q:
                curr = q.pop()
                for w in d[curr[-1]]:
                    if w == endWord:
                        curr_ans.append(curr + [w])
                    elif w not in seen:
                        tmp.append(curr+[w])
            
            for x in tmp:
                seen.add(x[-1])
            q.extend(tmp)
            if curr_ans:
                return curr_ans
            
        return []