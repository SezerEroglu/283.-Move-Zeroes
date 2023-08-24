from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonZeroIndex = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[nonZeroIndex], nums[i] = nums[i], nums[nonZeroIndex]
                nonZeroIndex += 1


# nums = [0, 1, 0, 3, 12]
nums = [0]
Solution.moveZeroes(Solution, nums)
print(nums)
