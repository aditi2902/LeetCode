class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)

        # Step 1: Find pivot
        pivot = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        # If no pivot found, array is descending
        if pivot == -1:
            nums.reverse()
            return

        # Step 2: Find smallest larger element from right
        for j in range(n - 1, pivot, -1):
            if nums[j] > nums[pivot]:
                nums[j], nums[pivot] = nums[pivot], nums[j]
                break

        # Step 3: Reverse suffix
        left = pivot + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1