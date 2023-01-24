class Solution:
    def plusOne(digits: list[int]) -> list[int]:
      if digits[-1] != 9:
        digits[-1] += 1
        return digits
      
      for i in range(len(digits) - 1, -1, -1):
        if digits[i] != 9:
          digits[i] += 1
          return digits

        digits[i] = 0
      
      digits.insert(0, 1)
      return digits


print(Solution.plusOne([9, 9]))