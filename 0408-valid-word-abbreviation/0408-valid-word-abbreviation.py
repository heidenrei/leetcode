class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n = len(word)
        i = 0
        for k, v in groupby(abbr, key=lambda x: x.isnumeric()):
            if k:
                v = list(v)
                if v[0] == '0':
                    return False
                #print(list(v))
                di = int(''.join(v))
                i += di
            else:
                v = list(v)
                print(i, v)
                di = 0
                while di + i < n and di < len(v):
                    if word[i+di] == v[di]:
                        di += 1
                    else:
                        print(word[i+di], abbr[di])
                        return False
                if di < len(v):
                    return False
                i += di
        
        return i == n
                