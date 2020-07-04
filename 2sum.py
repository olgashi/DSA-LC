class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in nums_dict:
                return {nums_dict[complement], i}
            nums_dict[nums[i]] = i


res = Solution()

print(res.two_sum([2, 7, 11, 15], 9))
