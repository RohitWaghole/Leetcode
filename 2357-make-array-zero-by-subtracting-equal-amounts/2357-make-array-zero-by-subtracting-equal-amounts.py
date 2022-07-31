class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            c = nums[i]
            for j in range(len(nums)):
                if nums[j]==0:
                    continue
                nums[j]-=c
            count+=1
            nums.sort()
            # print(nums)
        for i in range(len(nums)):
            if nums[i]!=0:
                count+=nums[i]
        return count