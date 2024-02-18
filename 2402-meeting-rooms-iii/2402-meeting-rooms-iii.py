from sortedcontainers import SortedList

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        #pq = SortedList([x for x in range(n)]) # available meeting rooms
        pq = [x for x in range(n)]
        c = defaultdict(list) # count of uses of each room
        events = SortedList() # meetings currently taking place (end time, room number)
        meeting_q = SortedList() # meetings waiting to take place (start time, end time)
        meetings.sort()
        
        for x, y in meetings:
            while events and events[0][0] <= x:
                events_end_time, room_num = events.pop(0)
                #pq.add(room_num)
                if len(pq) >= 1:
                    pq = [x for x in pq]
                    idx = bisect_left(pq, room_num)
                    pq = [w for w in pq[:idx]] + [room_num] + [x for x in pq[idx:]]
                else:
                    pq.append(room_num)
                while meeting_q and pq:
                    room_num = pq[0]
                    pq = pq[1:]
                    start_time, end_time = meeting_q.pop(0)
                    events.add([(end_time - start_time) + events_end_time, room_num])
                    
                    c[room_num].append([start_time, end_time])
                    
            if pq:
                room_num = pq[0]
                pq = pq[1:]
                events.add([y, room_num])
                c[room_num].append([x, y])
            else:
                meeting_q.add([x, y])

        while events:
            events_end_time, room_num = events.pop(0)
            if len(pq) >= 1:
                pq = [x for x in pq]
                idx = bisect_left(pq, room_num)
                pq = [x for x in pq[:idx]] + [room_num] + [w for w in pq[idx:]]
            else:
                pq.append(room_num)
            while meeting_q and pq:
                room_num = pq[0]
                pq = pq[1:]
                start_time, end_time = meeting_q.pop(0)
                events.add([(end_time - start_time) + events_end_time, room_num])
                c[room_num].append([start_time, end_time])
        
        best = 0
        maxi = 0
        for room_num in range(n):
            if len(c[room_num]) > maxi:
                maxi = len(c[room_num])
                best = room_num
                
        return best