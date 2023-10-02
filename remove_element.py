class Solution:
    def removeElement(nums: list[int], val: int) -> int:
        x = len(nums)
        i = 0
        while i <= x or i == 0:
            if nums[i] == val:
                nums.pop(i)
                x -= 1
                i -= 1
            else:
                i += 1
        return len(nums)
    
if __name__ == "__main__":
    print(Solution.removeElement([1], 1))