class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        n = len(nums)
        i = 0
        j = 0

        while i < n:
            if nums[i] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                j = j+1
            i= i+1

        # j = 0
        # for i in range(n):
        #     if nums[i]!= 0:
        #         nums[j],nums[i] = nums[i],nums[j]
        #         j = j+1
        