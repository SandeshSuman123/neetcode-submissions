class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,x in enumerate(nums):
            required=target-x
            if required in seen:
                return [seen[required], i]
            seen[x]=i
        
