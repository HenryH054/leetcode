"""Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:


If all assertions pass, then your solution will be accepted.
"""

class Solution:
    def removeElement(nums: list[int], val: int) -> int:
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                k += 1
                i += 1
        return k
    
if __name__ == "__main__":
    print(Solution.removeElement([1], 1))
    print(Solution.removeElement([], 5))
    print(Solution.removeElement([3, 2, 6, 2], 2))
    print(Solution.removeElement([1, 1, 1, 1], 1))        