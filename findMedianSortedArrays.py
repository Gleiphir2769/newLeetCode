from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n, A, B = len(nums1), len(nums2), nums1, nums2
        if m >= n:
            m, n, A, B = len(nums2), len(nums1), nums2, nums1

        i_min = 0
        i_max = m
        half_len = (m + n + 1) // 2

        while i_min <= i_max:
            i = (i_min + i_max) // 2
            j = half_len - i

            if i < m and B[j-1] > A[i]:
                i_min = i + 1
            elif i > 0 and A[i-1] > B[j]:
                i_max = i - 1
            else:
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 3], [2]))