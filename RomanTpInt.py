class Solution:
    def romanToInt(self, s: str) -> int:
        r2i = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        # i2r = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        res = 0
        while s is not "":
            if len(s) > 1:
                if r2i.get(s[0]) < r2i.get(s[1]):
                    r = s[:2]
                    s = s[2:]
                    res += r2i.get(r)
                else:
                    r = s[0]
                    s = s[1:]
                    res += r2i.get(r)
            else:
                res += r2i.get(s)
                s = ""
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("XXVII"))
