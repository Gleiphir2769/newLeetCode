class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        ans = 0
        hashset = set()
        while i != len(s) and j != len(s):
            if s[j] not in hashset:
                hashset.add(s[j])
                j += 1
                ans = max(ans, j-i)
            else:
                hashset.remove(s[i])
                i += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print("字符字串长度：", solution.lengthOfLongestSubstring("abcabcbb"))