class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        N = len(books)
        books.append(-1)
        mq = []
        dp = [0]*(N+1)
        for i in range(N):
            if books[i] > books[i-1]:
                dp[i] = dp[i-1] + books[i]
            else:
                curr = 0
                while 1:
                    if not mq:
                        curr = min(i, books[i])
                        extra = 0
                        break
                    j = mq[-1]
                    nj = books[i] - (i - j)
                    if books[j] >= nj:
                        mq.pop()
                    else:
                        curr = (i - j - 1)
                        extra = dp[j]
                        break
                s = (books[i] + books[i] - curr) * (curr + 1) // 2
                dp[i] = s + extra
            mq.append(i)
        return max(dp)