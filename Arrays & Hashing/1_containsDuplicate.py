# Explanation:
# Start by creating an empty set. Sets cannot contain duplicates of any item.
# For each element in the nums list, try adding it to the set.
# If the length of the set is less than the current index + 1,
# this means that the most recent add() call did not increase the length of the set,
# indicating there was an attempt to add an item that was already in the set.
# We return 'True' if this is the case, and if we get through the whole list without
# this occuring, there's no duplicates so we return 'False'.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         numSet = set()
         for idx, num in enumerate(nums):
            numSet.add(num)
            if len(numSet) < idx + 1:
                return True
         return False