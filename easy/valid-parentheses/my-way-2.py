class Solution:
    def isValid(s: str) -> bool:
      # print(ord(s[3]))
      if len(s) % 2 == 1 : return False

      for word in range(len(s)):
        char = ord(s[word])
        
        if chr(char) != ')' and chr(char) != '}' and chr(char) != ']':
          # print(chr(char))
          if s.count(chr(char + 2)) == 0 and s.count(chr(char + 1)) == 0:
            print(chr(char))
            return False

      return True

print(Solution.isValid("([)]"))