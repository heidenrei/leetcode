class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        out = []
        curr = ''
        for word in words:
            if len(curr) + len(word) + 1 > maxWidth:
                if curr:
                    out.append(curr)
                curr = word
            else:
                if curr:
                    curr += ' ' + word
                else:
                    curr = word
        
        
        if curr:
            out.append(curr)
        
        print(out)
        
        ans = []
        N = len(out)
        for idx, line in enumerate(out):
            spaces = line.count(' ')
            n = len(line.split(' '))
            needed_spaces = maxWidth - (len(line) - spaces)
            if needed_spaces == 0:
                ans.append(line)
                continue
            if n - 1 == 0:
                ans.append(line + ' '*needed_spaces)
                continue
            if idx == N-1:
                ans.append(line + ' '*(maxWidth-len(line)))
                break
            spaces_per = needed_spaces // (n - 1)
            line = line.split(' ')
            num_with_extra = needed_spaces - (spaces_per*(n-1))
            for i in range(len(line)-1):
                if i < num_with_extra:
                    line[i] += ' '*(spaces_per + 1)
                else:
                    line[i] += ' '*spaces_per
            ans.append(''.join(line))
            
        
        #print([len(x) for x in ans])
        
        return ans