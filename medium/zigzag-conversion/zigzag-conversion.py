def convert(self, s: str, numRows: int) -> str:
  if numRows <= 1: return s
  ans = ''
  count = 0
  	
  # 3rows
  # 1row = jump4
  # 2row = jump2
  # 3row = jump4

  # 4rows
  # 1row = jump6
  # 2row = jump4
  # 3row = jump2
  # 4row = jump6
  for i in range(numRows):
    count = i
    if count <= numRows - 2: jump = (((numRows - 1) * 2) - 2*count) 
    else: jump = ((numRows - 1) * 2)
    j = 0
    while True:
      try:
        pointer = jump*j
        ans += s[i + pointer]
        print(f'ans:{ans} count: {count}')
      except:
        break
      j += 1
      
  return ans 
    

print(convert(1, "PAYPALISHIRING", 4))
