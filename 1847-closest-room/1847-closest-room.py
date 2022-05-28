from sortedcontainers import SortedList

class Solution:
    def closestRoom(self, rooms, queries):
        N = len(rooms)
        Q = len(queries)
        ans = [inf for x in range(Q)]
        out = [-1 for x in range(Q)]
        queries = [[x[::-1], i] for i, x in enumerate(queries)]
        queries.sort(reverse=True)
        #print(queries)
        #print(queries)
        room_ids = SortedList()
        rooms = [[y,x] for x, y in rooms]
        rooms.sort()
        # print(queries)
        # print(rooms)
        for [size, pref], i in queries:
            while rooms and rooms[-1][0] >= size:
                rsize, roomid = rooms.pop()
                room_ids.add(roomid)
            # print(size, pref)
            # print(room_ids)
            # print()
            #idx = bisect_left(room_ids, pref)
            #print(size, pref)
            if size == 15 and pref == 15:
                print('1111', room_ids)
            idx = room_ids.bisect_left(pref)
            if idx - 1 >= 0 and idx - 1 < len(room_ids):
                if abs(room_ids[idx-1] - pref) < ans[i]:
                    ans[i] = abs(room_ids[idx-1] - pref)
                    out[i] = room_ids[idx-1]
            if idx < len(room_ids):
                if abs(room_ids[idx] - pref) < ans[i]:
                    ans[i] = abs(room_ids[idx] - pref)
                    out[i] = room_ids[idx]
                #ans[i] = min(ans[i], abs(room_ids[idx] - pref))

                #ans[i] = min(ans[i], abs(room_ids[idx-1] - pref))
            if idx + 1 < len(room_ids):
                if abs(room_ids[idx+1] - pref) < ans[i]:
                    ans[i] = abs(room_ids[idx+1] - pref)
                    out[i] = room_ids[idx+1]
                #ans[i] = min(ans[i], abs(room_ids[idx+1] - pref))
                
        return out