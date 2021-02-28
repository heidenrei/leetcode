class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        N = len(cars)
        D, V = zip(*cars)
        ans = [-1.0] * N
        
        print(D, V)
        
        # return how many seconds it takes to collid... difference in position / difference in speed, if rear car is faster
        def collision_point(i, j):
            d = D[j] - D[i]
            v = V[i] - V[j]
            return (d/v) if v else math.inf
        
        # stack holds the convex hull
        stack = []
        for i in range(N-1, -1, -1):
            while stack and V[stack[-1]] >= V[i] or (len(stack) >= 2 and collision_point(stack[-1], stack[-2]) < collision_point(i, stack[-1])):
                stack.pop()
            
            if stack:
                ans[i] = collision_point(i, stack[-1])
            stack.append(i)
            
        return ans