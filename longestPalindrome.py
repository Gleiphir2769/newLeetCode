class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        ans = s[0]
        for i in range(2*len(s) - 1):
            j = 0
            c_ans = ''
            while True:
                if i % 2 != 0:
                    left = (i - j - 1) / 2
                    right = (i + j + 1) / 2
                else:
                    left = (i - j) / 2
                    right = (i + j) / 2
                left = int(left)
                right = int(right)
                if left < 0 or right > len(s) - 1:
                    break
                if s[left] == s[right]:
                    c_ans = s[left:right+1]
                    j += 2
                else:
                    break
            ans = c_ans if len(c_ans) > len(ans) else ans

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("aa"))


