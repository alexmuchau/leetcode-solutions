from typing import List

def rotate(nums: List[int], k: int) -> None:
  for i in range(1, k  + 1):
    step = nums[-1]
    nums.pop()
    nums.insert(0, step)

rotate([1,2,3,4,5,6,7], 3)