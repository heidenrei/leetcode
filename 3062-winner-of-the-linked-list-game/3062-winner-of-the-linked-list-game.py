class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        res, node = 0, head
        
        # Iterate through the linked list
        while node:
            # Compare the current node's value with the next node's value
            if node.val > node.next.val:
                # If current value is greater, increment the result by 1
                res += 1
            else:
                # If current value is not greater, decrement the result by 1
                res -= 1
            # Move two steps forward in the linked list (skipping the next node)
            node = node.next.next
            
        # Determine the game result based on the final result
        return "Even" if res > 0 else "Tie" if res == 0 else "Odd"