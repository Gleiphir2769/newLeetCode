from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if nums[i] in map and target-nums[i] in map:
                return [map[target-nums[i]], i]
            elif nums[i] in map and target-nums[i] not in map:
                continue
            map[nums[i]] = i
            if i==0:
                continue

            if target-nums[i] in map and i != map[target-nums[i]]:
                return [i, map[target-nums[i]]]
        raise Exception("can't find!")

    def __init__(self):
        print("ok")


# if __name__ == '__main__':
#     # for i in range(5, 1, -1):
#     #     print(i)
#     # solution = Solution()
#     # print(solution.twoSum([2, 5, 5, 11], 10))


