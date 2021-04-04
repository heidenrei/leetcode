class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = defaultdict(set)
        
        for ID, time in logs:
            d[ID].add(time)
        
        UAM = [0]*k
        
        for k, v in d.items():
            UAM[len(v)-1] += 1
            
        return UAM
        
        
#         sets = [set() for x in range(k)]
        
#         logs.sort(key = lambda x: x[1])
        
#         for ID, time in logs:
#             sets[time-1].add(ID)
            
#         return [len(x) for x in sets]