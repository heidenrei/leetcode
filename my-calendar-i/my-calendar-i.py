from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        # sl[i] == [time, event_type]
        self.sl = SortedList()
        

    def book(self, start: int, end: int) -> bool:
        if self.sl:
            if start >= end:
                idx = self.sl.bisect([start, 1])
                if idx > 0:
                    if self.sl[idx-1][0] == start:
                        return False
                elif idx < len(self.sl)-1:
                    if self.sl[idx+1][0] == start:
                        return False
                else:
                    self.sl.add([start, 1])
                    self.sl.add([start, 0])
                    return True
                
            lidx = self.sl.bisect_right([start, 0])
            ridx = self.sl.bisect_left([end, 1])
            left = right = False

            if lidx != ridx:
                return False
            
            if (lidx == 0 or self.sl[lidx-1][1] == 0):
                left = True
            if ridx >= len(self.sl)-1 or self.sl[ridx][1] == 1:
                right = True
            
            if left and right:
                self.sl.add([start, 1])
                self.sl.add([end, 0])
                return True
            
            return False
        else:
            self.sl.add([start, 1])
            self.sl.add([end, 0])
            return True