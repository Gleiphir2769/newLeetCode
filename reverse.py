class Solution:
    def reverse(self, x: int) -> int:
        res = ''
        flag = ''
        real = False
        if x < 0:
            flag = '-'
            x = -x
        while x >= 10:
            y = x % 10
            x = x // 10
            if y != 0:
                real = True
            if real:
                res += str(y)
        res = int(flag + res + str(x))
        if -2147483648 < res < 2147483648 -1:
            return res
        else:
            return 0

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(0))