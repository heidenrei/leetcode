from sortedcontainers import SortedList

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        N = len(courses)
        h = SortedList()

        
        courses.sort(key=lambda x: (x[1], -x[0]))
        
        curr = 0
        ans = 0
        
        for d, e in courses:
            if d > e:
                continue
            if curr + d <= e:
                ans += 1
                curr += d
                h.add(d)
            else:
                if h[-1] > d:
                    curr -= h.pop()                    
                    h.add(d)
                    curr += d

        return ans