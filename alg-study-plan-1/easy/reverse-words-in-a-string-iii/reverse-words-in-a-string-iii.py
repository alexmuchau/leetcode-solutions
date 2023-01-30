def reverseWords(s: str) -> str:
  def sumStrings(a: str) -> str:
    return lambda x : x + " " + a
  
  reversedList = [x[::-1] for x in s.split(' ')]
  return [sumStrings(x) for x in reversedList]

print(reverseWords("Let's take LeetCode contest"))