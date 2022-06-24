class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff
'''class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
         
        diff = float('inf')
        nums.sort()
        ans = 0
        for i in range(len(nums)):
                
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeS = nums[i] + nums[l] + nums[r]
                d = abs(target - threeS)
                if d == 0:
                    return threeS
                
                if d < diff:
                    diff = d
                    ans = threeS
                
                if threeS < target:
                    l += 1
                else:
                    r -= 1
            
        return ans'''
        
