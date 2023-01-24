class Solution:
    def isValid(s: str) -> bool:
      # print(ord(s[3]))
      if len(s) % 2 == 1 : return False

      for word in range(0, len(s), 2):
        if ord(s[word]) != ord(s[word + 1]) - 1 and ord(s[word]) != ord(s[word + 1]) - 2:
          return False
      
      return True

print(Solution.isValid('()[]'))