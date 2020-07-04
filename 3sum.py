# # nums = [-1, 0, 1, 2, -1, -4]
# # nums = [-2,0,1,1,2]
# nums = [-1,0,1,2,-1,-4]
# solution_set = []
# solution = []
# result = []
# i = 0
# j = 1
# k = j + 1
# length = len(nums)
# while True:
#     if nums[i] + nums[j] + nums[k] == 0:
#         solution = [nums[i], nums[j], nums[k]]
#         solution.sort()
#         if solution not in solution_set:
#             solution_set.append(solution)
#     if i == length-3:
#         break
#     elif (j == length - 2) and (k == length - 1):
#         i += 1
#         j = i + 1
#         k = j + 1
#     elif k == length-1:
#         j += 1
#         k = j+1
#     else:
#         k += 1
#
# print(solution_set)
#
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0 or (lo > i + 1 and nums[lo] == nums[lo - 1]):
                lo += 1
            elif sum > 0 or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1


solution = Solution()

print(solution.threeSum([-1, 0, 1, 2, -1, -4]))