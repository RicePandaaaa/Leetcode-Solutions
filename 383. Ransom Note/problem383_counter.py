import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = collections.Counter(ransomNote)
        magazine_count = collections.Counter(magazine)

        for letter in ransom_count:
            if letter not in magazine_count or ransom_count[letter] > magazine_count[letter]:
                return False

        return True
