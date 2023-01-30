from typing import List

def search(nums: List[int], target: int) -> int:
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
            return mid
  
    return -1 

print(search([-1,0,3,5,9,12], 9))

