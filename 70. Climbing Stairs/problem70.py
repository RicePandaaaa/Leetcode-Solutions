class Solution:
    def climbStairs(self, n: int) -> int:
        # Preset values (obvious enough to calculate)
        steps = {1: 1, 2: 2}

        # If already calculated, go ahead and return
        if n in steps:
            return steps[n]

        # Otherwise, add the steps of n-1 and n-2
        for i in range(3, n+1):
            steps[i] = steps[i-2] + steps[i-1]

        return steps[n]
