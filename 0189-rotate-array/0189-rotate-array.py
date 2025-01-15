class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        def reversed(start :int, end: int) ->None:
            while(start<end):
                nums[start],nums[end] = nums[end],nums[start]
                start =  start + 1
                end = end - 1
        reversed(0,n-1)
        reversed(0,k-1) 
        reversed(k,n-1)      
        