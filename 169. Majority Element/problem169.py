# These imports are to avoid errors if ran in an IDE
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Edge case: only 1 element => return that element
        if len(nums) == 1:
            return nums[0]

        candidate = nums[0]
        count = 1

        # Since majority has more than half the votes, it will win out in a zero-sum style vote system
        for i in range(1, len(nums)):
            if count == 0:
                candidate = nums[i]

            if candidate == nums[i]:
                count += 1
            else:
                count -= 1

        return candidate
