class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        a = set(wordlist)
        b = defaultdict(list)
        d = defaultdict(list)
        vowels = {'a','e','i','o','u'}
        for word in wordlist:
            word_list_d = ''
            word_list_b = ''
            for ch in word:
                ch = ch.lower()
                word_list_b += ch
                if ch not in vowels:
                    word_list_d += ch
                else:
                    word_list_d += '!'
            b[word_list_b].append(word)
            d[word_list_d].append(word)
            
        ans = []
        for q in queries:
            if q in a:
                ans.append(q)
                continue
            tmp_b = ''
            for ch in q:
                tmp_b +=  ch.lower()
            if tmp_b in b:
                ans.append(b[tmp_b][0])
                continue
            tmp_d = ''
            for ch in tmp_b:
                if ch in vowels:
                    tmp_d += '!'
                else:
                    tmp_d += ch
            if tmp_d in d:
                ans.append(d[tmp_d][0])
                continue
        
            ans.append('')
            
        return ans