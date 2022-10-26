# This class represents a single word. It is made up of multiple syllables and its length
# can be measured in the number of syllables it has. Immutable class.


vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"


# Assume this is a valid input
def decompose_word(word):
    # This code would vary language to language. For now, let's assume always syllables
    # with monophthong vowels, with onsets and codas being at most one consonant but potentially null
    # If there is a consonant between two vowels, it is assumed to be a onset by default

    syllables = []

    left_pointer = 0
    right_pointer = 0
    while left_pointer < len(word):
        if word[right_pointer] in vowels:
            if word[right_pointer + 1] in vowels: # Null coda, next syllable null onset
                syllables.append(word[left_pointer:right_pointer + 1] )
            elif word[right_pointer + 2] in vowels: # Null coda, next syllable non-null onset
                syllables.append(word[left_pointer:right_pointer + 1] )
            else: # Non-null coda
                syllables.append()







class Word:
    def __init__(self, word):
        self.syllables = []
        self.num_syllables = 0
