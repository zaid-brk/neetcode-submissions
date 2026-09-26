class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        prev, curr = 1, 1
        for i in range(1, n):
            nxt = prev + curr
            prev = curr
            curr = nxt
        return curr