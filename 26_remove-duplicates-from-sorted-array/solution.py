class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        for p in range (1,len(nums)):
            if nums[p] != nums[p-1]:
                nums[k]=nums[p]
                k+=1
        return k