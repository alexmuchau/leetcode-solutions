from typing import List

def removeElement(nums: List[int], val: int) -> int:
  nums.sort()
  quantity = nums.count(val)
  for _ in range(quantity):
    nums.remove(val)
  
  return nums

print(removeElement([4, 5, 12, 23, 5, 2 ,3, 6 , 4 ,5 , 5, 5 ,5 ,2 , 1], 5))

