class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        s = ''
        for x in strs:
            for y in x:
                s += str(ord(y))
                s += '_'
            if s and s[-1] == '_':
                s = s[:-1]
            s += ' '
        if s and s[-1] == ' ':
            s = s[:-1]
        return s
                
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        #print(s)
        for x in s.split(' '):
            tmp = ''
            for y in x.split('_'):
                if not y:
                    continue
                tmp += chr(int(y))
            ans.append(tmp)
        return ans


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))