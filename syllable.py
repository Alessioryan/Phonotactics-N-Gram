# This class represents a syllable. Word s are made up of various instances of this class. Immutable class.


# For now no phoneme class, but we can go back and add it later


vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"


# Assume this is a valid input
def decompose_syllable(syllable):
    # This code would vary language to language. For now, let's assume always syllables
    # with monophthong vowels, with onsets and codas being at most one consonant but potentially null

    syllable_parts = []
    for letter in vowels:
        if letter in syllable:
            vowel_index = syllable.index(letter)
            syllable_parts[0] = syllable[0:vowel_index]
            syllable_parts[1] = syllable[vowel_index]
            syllable_parts[2] = syllable[vowel_index + 1:]
    return syllable_parts


class Syllable:
    def __init__(self, syllable):
        self.syllable_parts = decompose_syllable(syllable)
