# This class represents a syllable. Word s are made up of various instances of this class. Immutable class.


# For now no phoneme class, but we can go back and add it later


vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"


# Assume this is a valid input
def decompose_syllable_ex1(syllable):
    # This code would vary language to language. For now, let's assume always syllables
    # with monophthong vowels, with onsets and codas being at most one consonant but potentially null

    syllable_parts = []
    for letter in vowels:
        if letter in syllable:
            vowel_index = syllable.index(letter)
            syllable_parts.append(syllable[0:vowel_index] )
            syllable_parts.append(syllable[vowel_index] )
            syllable_parts.append(syllable[vowel_index + 1:] )
    return syllable_parts


class Syllable:
    def __init__(self, syllable):
        self.syllable_parts = decompose_syllable(syllable)

    def __str__(self):
        return str(self.syllable_parts)


if __name__ == '__main__':
    test_syllable = Syllable("tes")
    print(test_syllable)
