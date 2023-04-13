class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        N = len(pushed)
        stack = []
        
        popped = deque(popped)
        
        for i in range(N):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[0]:
                popped.popleft()
                stack.pop()
                
        return not stack