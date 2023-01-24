from typing import List

class Solution:
  def getConcatenation(self, nums: List[int]) -> List[int]:
    ans = nums*2
    return ans

print(Solution.getConcatenation(1, [1,2,3]))