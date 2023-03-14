from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    if len(nums) == 0: return [-1, -1]
    if len(nums) == 1 and nums[0] == target: 
      return [0, 0] 
    elif len(nums) == 1 and nums[0] != target:
      return [-1, -1] 
    
    low = 0  
    high = len(nums) - 1  
    mid = 0  
  
    while low <= high:  
        print(f"mid: {mid} high: {high} low: {low}")
        mid = (high + low) // 2  
  
        if nums[mid] < target:  
            low = mid + 1  
  
        elif nums[mid] > target:  
            high = mid - 1 
  
        else:  
            break
    
    if nums[mid] != target: return [-1, -1]
    if nums[mid + 1] != target and nums[mid - 1] != target: return [mid, mid]

    for i in range(mid + 1, len(nums), 1):
      if nums[i] != target:
        high = i - 1
        break
    for i in range(mid - 1, -1, -1):
      if nums[i] != target:
        low = i + 1
        break

    return [low, high]

print(searchRange([], 8))