# This class represents a single word. It is made up of multiple syllables and its length
# can be measured in the number of syllables it has. Immutable class.

from syllable import Syllable

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"


# Assume this is a valid input
def decompose_word(word):
    # This code would vary language to language. For now, let's assume always syllables
    # with monophthong vowels, with onsets and codas being at most one consonant but potentially null
    # If there is a consonant between two vowels, it is assumed to be a onset by default
    word += "XXX"
    syllables = []
    while len(word) > 0:
        temp_syllable = ""
        if word[0] == "X":
            break
        if word[0] in consonants: # Add optional onset
            temp_syllable += word[0]
            word = word[1:]
        temp_syllable += word[0] # Add nucleus
        word = word[1:]
        # If neither of the following two cases
        # Null coda, next syllable null onset (case 1)
        # Null coda, next syllable non-null onset (case 2)
        if word[0] not in vowels and word[1] not in vowels:
            temp_syllable += word[0]
            word = word[1:]
        syllables.append(temp_syllable.strip("X") )
    return syllables


class Word:
    def __init__(self, word):
        self.original_word = word.lower()
        self.syllables = []
        for text_syllable in decompose_word(self.original_word):
            self.syllables.append(Syllable(text_syllable) )
        self.num_syllables = len(self.syllables)

    # Kinda janky print but it works ig
    def __str__(self):
        syllable_list = []
        for syllable in self.syllables:
            syllable_list.append(str(syllable) )
        return self.original_word + " is " + str(syllable_list).replace("\"", "")


if __name__ == '__main__':
    test_word = Word("testo")
    print(test_word)
