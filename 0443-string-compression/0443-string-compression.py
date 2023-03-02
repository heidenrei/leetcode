class Solution:
    def compress(self, chars: List[str]) -> int:
        curr = chars[0]
        cnt = 1
        ans = ''
        for x in chars[1:]:
            if x != curr:
                if cnt == 1:
                    ans += curr
                else:
                    ans += curr + str(cnt)
                cnt = 1
            else:
                cnt += 1
            curr = x
        ans += curr
        if cnt > 1:
            ans += str(cnt)
        #print(ans)
        for i in range(len(ans)):
            chars[i] = ans[i]
        while len(chars) > len(ans):
            chars.pop()
        return len(chars)