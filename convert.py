class Solution:
    def convert(self, s:str, numRows: int) -> str:
        if numRows < 2:
            return s
        i, flag = 0, -1
        res = ['' for _ in range(numRows)]
        for c in s:
            res[i] += c
            if i == numRows-1 or i == 0:
                flag = -flag
            i += flag
        return "".join(res)

if __name__ == '__main__':
    s = Solution()
    print(s.convert("abc", 2))