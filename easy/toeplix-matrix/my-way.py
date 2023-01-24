class Solution:
    def isToeplitzMatrix(matrix: list[list[int]]) -> bool:
      for i in range(len(matrix[0]) - 1, 0, -1):
        j = 1
        firstNum = matrix[j][i]
        while i < len(matrix[0]) and j < len(matrix):
          if matrix[j][i] != firstNum:
            return False
          i += 1
          j += 1

      for i in range(len(matrix) - 2, 0, -1):
        j = 1
        firstNum = matrix[j][i]
        while i < len(matrix):
          i += 1
          print(matrix[i][i])
          if matrix[i][i] != firstNum:
            return False
      
      return True

print(Solution.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))