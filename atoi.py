import re
class Solution:
    def myAtoi(self, str: str) -> int:
        isSymbol = False
        isNumber = False
        res = ''
        sym = '+'
        for c in str:
            if c == ' ' and not isNumber and not isSymbol:
                continue
            if (c == '+' or c == '-') and not isSymbol and not isNumber:
                isSymbol = True
                sym = c
                continue
            if c.isdigit():
                isNumber = True
                res += c
                continue
            break
        if isNumber:
            if isSymbol and sym == '-':
                res = sym + res
            return max(min(int(res), 2**31-1), -2**31)
        return 0

# class Solution:
#     def myAtoi(self, s: str) -> int:
#         # [\+\-]? 表示匹配一个或零个该模式，非贪婪
#         return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)



if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("99999999999999999"))