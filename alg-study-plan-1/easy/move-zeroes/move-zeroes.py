from typing import List

def moveZeroes(nums: List[int]) -> None:
  nums.sort()
  count = nums.count(0)
  if count == 0: return nums.sort()

  nums = nums[::count]
  # for _ in range(count): nums.append(0)
  print(nums)

moveZeroes([0,1,0,3,12])

  
