class Solution:
    def longestPrefix(strs: list[str]) -> str:
        if len(strs) == 0: return ""
        
        longPref = strs[0]
        
        for string in strs:
            for index in range(0, len(longPref)):
                if (index >= len(string) or longPref[index] != string[index]):
                    longPref = longPref[0:index]
                    break
                
        return longPref

print(Solution.longestPrefix(["flor", "flow", "flight"]))