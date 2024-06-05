class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_letters = list(ransomNote)
        magazine_letters = list(magazine)

        for i in range(len(ransom_letters)):
            letter = ransom_letters[i]

            if letter in magazine_letters:
                magazine_letters.remove(letter)

            else:
                return False

        return True
