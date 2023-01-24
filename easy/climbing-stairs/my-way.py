class Solution:
    def climbStairs(self, n: int) -> int:
        previous = 1
        current = 1
        for i in range(n - 1):
            current += previous
            previous = current - previous

        return current
        

print(Solution.climbStairs(Solution(), 21))
        