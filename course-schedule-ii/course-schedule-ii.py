class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.prereqs = collections.defaultdict(set)
        self.N = numCourses
        self.out = []
        self.num_prereqs = [0] * self.N # how many prereqs each course has
        for c, p in prerequisites:
            self.prereqs[p].add(c) # key = prereqs, value = courses that can be taken once prereqs met
            self.num_prereqs[c] += 1
        print(self.prereqs)
        print(self.num_prereqs)
        self.q = collections.deque()
        
        self.go()
        if len(self.out) == self.N:
            return self.out
        return []
    def go(self):
        for i in range(self.N):
            if self.num_prereqs[i] == 0:
                self.q.append(i)
                
        while len(self.q) > 0:
            tmp = self.q[0]
            self.q.popleft()
            self.out.append(tmp)
            for child in self.prereqs[tmp]:
                self.num_prereqs[child] -= 1
                if self.num_prereqs[child] == 0:
                    self.q.append(child)