from textwrap import wrap

class Solution:
    def romanToInt(s: str) -> int:
      romanToNumbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
      }

      exclusiveCases = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
      }
      
      if len(s) == 2 and s in exclusiveCases:
        print(exclusiveCases[s])
        return exclusiveCases[s]

      answer = 0
      exclusive = -1

      for i in range(len(s) - 1):
        word = s[i]

        if word + s[i + 1] in exclusiveCases:
          answer += exclusiveCases[word + s[i + 1]]
          # print(word + s[i + 1])
          exclusive = i + 1
        else:
          if exclusive == i:
            continue

          answer += romanToNumbers[word]
          # print(word)
      
      if exclusive != len(s) - 1:
        answer += romanToNumbers[s[len(s) - 1]]

      print(answer)
      return answer

Solution.romanToInt("MCMXCIV")  
        