from typing import List

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
  sortedLists = sorted(nums1 + nums2)
  sumOfLens = len(sortedLists)
  if sumOfLens % 2 == 0:
    return (sortedLists[sumOfLens // 2 - 1] + sortedLists[sumOfLens // 2]) / 2
  else:
    return sortedLists[sumOfLens // 2]

print(findMedianSortedArrays(1, [1, 2], [3]))

