class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Check if len is diff, if so we know for sure it is false
        if len(s) != len(t):
            return False

        sCounts = {}
        tCounts = {}
        for idx in range(len(s)):
            if s[idx] not in sCounts:
                sCounts[s[idx]] = 1
            else:
                sCounts[s[idx]] += 1
            
            if t[idx] not in tCounts:
                tCounts[t[idx]] = 1
            else:
                tCounts[t[idx]] += 1
            
        for k, v in sCounts.items():
            if k not in tCounts: return False

            if tCounts[k] != v: return False
        
        for k, v in tCounts.items():
            if k not in sCounts: return False

            if sCounts[k] != v: return False


        return True
