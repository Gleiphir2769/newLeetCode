from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_pre = ''
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        while True:
            index = len(strs)
            temp = ''
            for i in range(len(strs)):
                s = strs[i]
                if s == "":
                    break
                if temp == '':
                    temp = s[0]
                    strs[i] = s[1:]
                    index -= 1
                elif s[0] == temp:
                    strs[i] = s[1:]
                    index -= 1
                else:
                    break
            if index == 0:
                longest_pre += temp
            else:
                break
        return longest_pre


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["ab", "abc"]))
