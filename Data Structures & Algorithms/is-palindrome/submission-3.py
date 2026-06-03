class Solution:
    def isPalindrome(self, s: str) -> bool:

        # nonWhiteSpaces = s.replace(' ', '')
        # nonWhiteSpaces = nonWhiteSpaces.replace('.', '')
        # nonWhiteSpaces = nonWhiteSpaces.replace('?', '')
        # nonWhiteSpaces = nonWhiteSpaces.replace(',', '')
        # nonWhiteSpaces = nonWhiteSpaces.replace("'", '')
        nonWhiteSpaces = "".join(char for char in s if char.isalnum())

        lPtr = 0
        rPtr = len(nonWhiteSpaces) - 1
        while lPtr < rPtr:
            print(nonWhiteSpaces[lPtr].lower(), nonWhiteSpaces[rPtr].lower())
            if nonWhiteSpaces[lPtr].lower() == nonWhiteSpaces[rPtr].lower():
                lPtr += 1
                rPtr -= 1
            else: return False
        return True