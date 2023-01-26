def firstBadVersion(n: int) -> int:
    low = 0  
    high = n  
    mid = 0  
  
    while True:  
      mid = (high + low) // 2  
  
      if isBadVersion(mid) == False:  
        low = mid + 1  
  
      elif isBadVersion(mid) == True:  
        high = mid - 1 
      
      if isBadVersion(low) == True:
        return low
