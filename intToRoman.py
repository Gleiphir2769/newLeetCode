class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        while num > 0:
            if num - 1000 >= 0:
                num -= 1000
                res += "M"
            elif num - 900 >= 0:
                num -= 900
                res += "CM"
            elif num - 500 >= 0:
                num -= 500
                res += "D"
            elif num - 400 >= 0:
                num -= 400
                res += "CD"
            elif num - 100 >= 0:
                num -= 100
                res += "C"
            elif num - 90 >= 0:
                num -= 90
                res += "XC"
            elif num - 50 >= 0:
                num -= 50
                res += "L"
            elif num - 40 >= 0:
                num -= 40
                res += "XL"
            elif num - 10 >= 0:
                num -= 10
                res += "X"
            elif num - 9 == 0:
                num -= 9
                res += "IX"
            elif num - 5 >= 0:
                num -= 5
                res += "V"
            elif num - 4 == 0:
                num -= 4
                res += "IV"
            elif num - 1 >= 0:
                num -= 1
                res += "I"
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(1999))