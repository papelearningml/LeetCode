class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p=len(nums)-1
        b=0
        k=0
        while p1 < len(nums):
            if nums[p1] == val:
                #nums[p]=0
                p-=1
                p1+=1
            else:
                nums[b]=nums[p1]
                b+=1
                p1+=1
                k+=1

        return k