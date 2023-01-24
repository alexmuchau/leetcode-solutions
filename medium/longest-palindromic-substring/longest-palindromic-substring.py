def longestPalindrome(s: str) -> str:
  if s == s[::-1]: return s

  length = len(s)
  answer = ''
  
  for i in range(length):
    j = s[i:length]
    if j == j[::-1] and len(j) > len(answer): 
      answer = j
      continue

    for k in range(i + 1, length, 1):
      j = s[i:k]
      if j == j[::-1] and len(j) > len(answer): 
        answer = j
        continue

  return answer

print(longestPalindrome('cbbd'))