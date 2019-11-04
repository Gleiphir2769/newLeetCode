class Solution:
    def isPalindrome(self, x: int) -> bool:
        sx = str(x)
        re_sx = sx[::-1]
        if sx == re_sx:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(-11211))

