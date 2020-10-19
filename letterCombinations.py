from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        reflect = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
                   6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 1: ['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']}
        digits = digits.replace('1', '')
        digits = digits.replace('8', '1')
        if len(digits) > 1:
            nums = list(digits)
        else:
            if digits == '':
                return []
            else:
                index = int(digits[0])
                return reflect.get(index)
        check_list = []
        res_count = 1
        for index, num in enumerate(nums):
            if int(num) == 7 or int(num) == 9:
                count = 4
            else:
                count = 3
            res_count = res_count*count
            if index == 0:
                check_list = reflect[int(num)]
                continue
            temp_list = []
            chars = reflect.get(int(num))
            for check_char in check_list:
                for char in chars:
                    temp_list.append(check_char+char)
            check_list = temp_list
        print(res_count)
        return check_list[-res_count:]


if __name__ == '__main__':
    solution = Solution()
    res = solution.letterCombinations('32')
    print(res)