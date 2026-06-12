class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_checkset = set()
        for num in nums:
            if num in nums_checkset:
                return True
            
            nums_checkset.add(num)
        return False