class Solution:
    def isValid(s: str) -> bool:
        map = {')':'(', '}':'{', ']':'['}
        st = []
        for c in s:
            if len(st)==0 or not c in map.keys():
                st.append(c)
            elif map.get(c)==st[-1]:
                st.pop()
            else:
                print(c)
                st.append(c)
        return len(st)==0

print(Solution.isValid("([])"))