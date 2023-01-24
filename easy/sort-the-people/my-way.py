class Solution:
    def sortPeople(names: list[str], heights: list[int]) -> list[str]:
      sortHeights = [heights[0]]
      answer = [names[0]]
      for height in range(1, len(heights)):
        for i in range(len(sortHeights)):
          if heights[height] > sortHeights[i]:
            sortHeights.insert(i, heights[height])
            answer.insert(i, names[height])
            break

        if i == len(sortHeights) - 1:
          sortHeights.append(heights[height])
          answer.append(names[height])
      
      return(answer)
print(Solution.sortPeople(["Mary","John","Emma"], [155,175,185]))