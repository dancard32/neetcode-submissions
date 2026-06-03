class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

        result = []
        while len(result) < k:
            max_freq = 0
            most_common_num = None
            for num, freq in count_map.items():
                if freq > max_freq:
                    max_freq = freq
                    most_common_num = num
            result.append(most_common_num)
            del count_map[most_common_num]

        return result

