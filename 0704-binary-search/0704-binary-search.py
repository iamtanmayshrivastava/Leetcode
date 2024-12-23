class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)-1
        start = 0
        end = size-1
        while(start<=end):
            mid = (start+end)//2
            if nums[mid]== target:
                return mid
            elif(nums[mid] > target):
                end = mid-1
            elif(nums[mid] <target):
                start = mid+1
        return -1


