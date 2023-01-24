class Solution:
    def lengthOfLastWord(s: str) -> int:
      return len(s.strip().split()[-1])
        
print(Solution.lengthOfLastWord("   fly me   to   the moon  "))