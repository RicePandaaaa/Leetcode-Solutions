# These imports are to avoid errors if ran in an IDE
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: list has 0 or 1 item(s) => do nothing since list can't have duplicates
        if len(nums) < 2:
            return len(nums)

        # Keep track of index of current number
        current_index = 0

        for i in range(1, len(nums)):
            # Once a different number is found, place it right after the current number
            if nums[current_index] != nums[i]:
                current_index += 1
                nums[current_index] = nums[i]

        # The index is 0-based so add 1
        return current_index + 1
