class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        N = len(message)
        def is_good(x):
            ans = []
            tmp = ''
            cnt = 1
            curr_len = x
            i = 0
            good = True
            while i < N:
                while i < N and len(tmp) < curr_len:
                    tmp += message[i]
                    i += 1
                tmp += '<' + str(cnt) + '/_>'
                ans.append(tmp)
                tmp = ''
                
                if i == N:
                    for j in range(len(ans)):
                        ans[j] = ans[j].replace('_', str(cnt))
                        # if len(ans[j-1]) != limit:
                        #     return []
                    return ans
                else:
                    #i += 1
                    if len(set([x for x in str(cnt)])) == 1 and str(cnt)[-1] == '9':
                        curr_len -= 1
                    if curr_len == 0:
                        #print('111', ans)
                        return []
                    cnt += 1
            #print('222', ans)
            return []
        
        l, r = 1, limit - 5
        
        for m in range(r, l-1, -1):
            ans = is_good(m)

            if ans and all([len(x) == limit for x in ans[:-1]]):
                return ans
        return []
#         while l < r:
#             m = l + r >> 1
#             if is_good(m):
#                 l = m + 1
#             else:
#                 r = m - 1
        
#         ans = is_good(r)
#         if all([len(x) == limit for x in ans[:-1]]):
#             return ans
#         return is_good(r-1)