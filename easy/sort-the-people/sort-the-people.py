class Solution:
    def sortPeople(names: list[str], heights: list[int]) -> list[str]:
        tempLi = sorted(heights, reverse = True)
        ans = []
        for i in tempLi:
            ans.append(names[heights.index(i)])
        return ans

print(Solution.sortPeople(["Mary","John","Emma"], [155,175,185]))