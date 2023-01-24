class Solution:
    def searchInsert(nums: list[int], target: int) -> int:
      if nums.count(target) > 0:
        return nums.index(target)
      else:
        nums.append(target)
        nums.sort()
        return nums.index(target)

print(Solution.searchInsert([1,3,5,6], 7))