class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        N = len(intervals)
        
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = []
        
        high = intervals[0][1]
        low = intervals[0][0]
        
        for i in range(1, N):
            if high >= intervals[i][0]:
                high = max(high, intervals[i][1])
            else:
                ans.append([low, high])
                high = intervals[i][1]
                low = intervals[i][0]
            
        ans.append([low, high])   
            
        return ans