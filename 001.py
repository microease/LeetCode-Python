# 1. 两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

nums = [2, 7, 11, 15]
target = 9


# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if j > i:
#                     if nums[j] == target - nums[i]:
#                         return i, j
# s = Solution()
# print(s)
res = enumerate(nums)
for i,j in res:
    print(i,j)
print(res)
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None
s = Solution()