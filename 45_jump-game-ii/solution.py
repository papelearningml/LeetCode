class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_reach = 0
        current_end=0
        jumps=0

        if n<=1: return 0

        for i in range(n-1):

            max_reach = max(max_reach, i+nums[i])

            if i == current_end:
                jumps+=1
                current_end = max_reach

                if current_end >= n-1:
                    break

        return jumps

            
            