class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        N = len(books)
        
        @cache
        def go(i, rem, currh):
            if i == N:
                return 0
            
            if books[i][0] <= rem:
                cost = 0
                if books[i][1] > currh:
                    cost = books[i][1] - currh
                same_row = go(i+1, rem - books[i][0], max(currh, books[i][1])) + cost
            else:
                same_row = inf
            
            new_row = go(i+1, shelfWidth - books[i][0], books[i][1]) + books[i][1]
            
            return min(new_row, same_row)
        
        return go(0, shelfWidth, 0)
            
            