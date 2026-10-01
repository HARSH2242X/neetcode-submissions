class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k =k%n
        if(len(nums)==0 or len(nums) ==1):
            return nums
        nums[:] = nums[-k:] + nums[:-k]


        """
        Do not return anything, modify nums in-place instead.
        """
        