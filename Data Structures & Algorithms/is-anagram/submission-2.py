class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        s_dict = {}
        t_dict = {}
        for idx in range(len(s)):
            s_char = s[idx]
            t_char = t[idx]

            if s_char not in s_dict:
                s_dict[s_char] = 1
            else:
                s_dict[s_char] += 1
    
            if t_char not in t_dict:
                t_dict[t_char] = 1
            else:
                t_dict[t_char] += 1
        
        if t_dict.keys() != s_dict.keys(): return False

        for k, v in s_dict.items():
            if v != t_dict[k]: return False

        return True
