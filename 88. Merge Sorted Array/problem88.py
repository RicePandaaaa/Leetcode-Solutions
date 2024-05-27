# These imports are to avoid errors if ran in an IDE
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Edge case: m is 0 => nums1 becomes nums2
        if m == 0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]

        # Edge case: n is 0 => do nothing
        elif n == 0:
            pass

        # Normal case: check every number and insert as needed
        else:
            numbers_processed = 0
            nums1_index = 0
            nums2_index = 0

            while numbers_processed < m + n and nums2_index < len(nums2):
                current_num1 = nums1[nums1_index]
                current_num2 = nums2[nums2_index]

                # If the index exceeds exceeds the number of pre-existing values, just replace and increment both indicies
                if nums1_index == m + nums2_index:
                    nums1[nums1_index] = nums2[nums2_index]
                    nums1_index += 1
                    nums2_index += 1

                # else If current_num1 < current_num2, just increment to next index in nums1
                elif current_num1 < current_num2:
                    nums1_index += 1

                # else, insert current_num2, increment both indices, and remove last 0
                else:
                    nums1.insert(nums1_index, current_num2)
                    nums1_index += 1
                    nums2_index += 1

                    nums1.pop()

                # Regardless, a number was processed
                numbers_processed += 1


