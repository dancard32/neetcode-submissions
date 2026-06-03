class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        sortedUniqueNumbers = sorted(list(set(nums)))

        longestSequence = 0
        sequenceQueue = [sortedUniqueNumbers[0]]
        for num in sortedUniqueNumbers:
            if num - 1 == sequenceQueue[-1]:
                sequenceQueue.append(num)
            else:
                sequenceQueue = [num]

            if len(sequenceQueue) > longestSequence:
                longestSequence = len(sequenceQueue)
            

        return longestSequence
        