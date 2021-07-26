from sortedcontainers import SortedList

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = SortedList()
        chairs = SortedList([x for x in range(10**4)])
        i_to_chair = defaultdict(int)
        for i, x in enumerate(times):
            events.add([x[0], 1, i])
            events.add([x[1], 0, i])
            
        for t, e, i in events:
            if e == 1:
                if i == targetFriend:
                    return chairs.pop(0)
                chair = chairs.pop(0)
                i_to_chair[i] = chair
            else:
                chair = i_to_chair[i]
                chairs.add(chair)
                
        