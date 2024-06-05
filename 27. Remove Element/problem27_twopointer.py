# These imports are to avoid errors if ran in an IDE
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int):
        # Keep track of where the value is
        val_index = 0

        for i in range(len(nums)):
            # If found a number that is not the value, swap it with the left-most occurance of the value
            if nums[i] != val:
                nums[val_index] = nums[i]
                val_index += 1

        return val_index
