# These imports are to avoid errors if ran in an IDE
from typing import List


class Solution:
    def reverse(self, nums: List[int], start: int, end: int):
        """
        Helper function to reverse a list
        """
        left = start
        right = end

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
    def rotate(self, nums: List[int], k: int) -> None:
        # Ensure k is less than len(nums)
        k %= len(nums)

        # Reverse the whole list
        self.reverse(nums, 0, len(nums)-1)

        # Reverse the first k elements
        self.reverse(nums, 0, k-1)

        # Reverse everything else
        self.reverse(nums, k, len(nums)-1)
