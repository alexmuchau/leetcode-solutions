class Solution:
    def searchInsert(nums: list[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums.sort()      
        return nums.index(target)

print(Solution.searchInsert([1,3,5,6], 7))