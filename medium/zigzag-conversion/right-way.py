def convert(self, s: str, numRows: int) -> str:
    template = list(range(numRows)) + list(range(numRows - 2, 0, -1))
    print(template)

    result = [''] * numRows
    for i, char in enumerate(s):
        print(f"i {i} char {char} = i % len(template) {i % len(template)}")
        result[template[i % len(template)]] += char
    return ''.join(result)

print(convert(1, "PAYPALISHIRING", 4))