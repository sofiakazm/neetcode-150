class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, num in enumerate(nums):
            res = numMap.get(target - num)
            if res != None:
                return[res, i]
            numMap[num] = i