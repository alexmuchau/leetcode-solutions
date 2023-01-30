from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  seen = {}
  for idx in range(len(nums)):
    remaining = target - nums[idx]
    if remaining in seen:
      return [seen[remaining]+1, idx+1]
    seen[nums[idx]] = idx

print(twoSum([2,11,15], 18))