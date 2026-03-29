class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        len_ = len(nums)
        nums.sort()

        if len_ % 2 == 0:
            return (nums[int(len_ / 2 - 1)] + nums[int(len_ / 2)] ) / 2
        else:
            return nums[int(len_ / 2)]