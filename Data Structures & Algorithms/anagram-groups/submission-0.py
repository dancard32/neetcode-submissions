class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str not in anagram_map:
                anagram_map[sorted_str] = [s]
            else:
                anagram_map[sorted_str].append(s)
        return list(anagram_map.values())
