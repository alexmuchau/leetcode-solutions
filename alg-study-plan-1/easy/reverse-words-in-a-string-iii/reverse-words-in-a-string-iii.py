def reverseWords(s: str) -> str:
  reversedList = [x[::-1] for x in s.split(' ')]
  answer = reversedList[0]

  for i in range(1, len(reversedList)):
    answer += " " + reversedList[i]

  return answer

print(reverseWords("Let's take LeetCode contest"))