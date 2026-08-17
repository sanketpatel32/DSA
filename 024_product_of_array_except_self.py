"""
024_product_of_array_except_self

Question:
output[i] = product of all except nums[i], without division, in O(n).

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Approaches:
  1. Division: total product / nums[i] (handle zeros)  ->  O(n) time, O(1) extra space
  2. Left and right prefix product arrays  ->  O(n) time, O(n) space
  3. Single output array with running prefix (left then right sweep)  ->  O(n) time, O(1) extra space
"""

from turtle import right


def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n
    left = [1] * n
    right = [1] * n

    for i in range(n):
        answer[i] *= left[i]
        left[i] *= nums[i]

    for i in range(n - 1, -1, -1):
        answer[i] *= right[i]
        right[i] *= nums[i]

    return answer


# ---- Quick test ----
if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([2, 3, 4, 5], [60, 40, 30, 24]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ]
    for nums, expected in tests:
        result = productExceptSelf(nums)
        print(
            f"nums={nums} -> {result} {'PASS' if result == expected else 'FAIL expected ' + str(expected)}"
        )
