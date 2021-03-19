class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        if N <= 1:
            return True
        # jus tneed bfs
        seen = set([0])
        q = deque([0])
        while q:
            tmp = []
            while q:
                key = q.pop()
                for new_key in rooms[key]:
                    if new_key not in seen:
                        seen.add(new_key)
                        tmp.append(new_key)
                        if len(seen) == N:
                            return True
            q.extend(tmp)
        
        return False