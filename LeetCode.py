# class Solution(object):
#     def twosum(self, nums, target):
#         nums_dict = {}
#         for i, num in enumerate(nums):
#             x = target - num
#             if x in nums_dict:
#                 return [nums_dict[x], i]
#
#             nums_dict[num]= i
#
#         return
#
#
# nums = [2, 7, 11, 15]
# target = 13
# output = Solution()
# r = output.twosum(nums, target)
# print(r)