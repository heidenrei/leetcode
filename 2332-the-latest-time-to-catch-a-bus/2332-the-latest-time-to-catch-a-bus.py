class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], cap: int) -> int:
        events = []
        for x in buses:
            events.append([x, 1])
        for x in passengers:
            events.append([x, 0])
        used = set(passengers)
        free = set()
        for x in used:
            if x-1 not in used:
                free.add(x-1)
        for x in buses:
            if x not in used:
                free.add(x)
        #print(free)
        for x in free:
            events.append([x, 0])
        
        events.sort()
        # need to be last person on last bus
        q = []
        max_free = 0
        for x, t in events:
            if t == 1:
                #print(x, q)
                #max_free = 0
                cnt = 0
                while q and cnt < cap:
                    tmp = heappop(q)
                    if tmp in used:
                        cnt += 1
                    else:
                        #print('111', tmp)
                        max_free = tmp
            else:
                heappush(q, x)
        return max_free
                    