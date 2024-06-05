# These imports are to avoid errors if ran in an IDE
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int):
        while val in nums:
            nums.remove(val)

        return len(nums)
