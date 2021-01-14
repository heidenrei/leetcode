class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        N = len(people)
        people.sort(reverse=True)
        people = deque(people)
        cnt = 0
        
        while len(people) > 1:
            heavy = people.popleft()
            light = people.pop()
            
            if heavy + light > limit:
                people.append(light)
                
            cnt += 1
            
        cnt += len(people)
        
        return cnt
