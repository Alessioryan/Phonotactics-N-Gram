# This class represents a single word. It is made up of multiple syllables and its length
# can be measured in the number of syllables it has. Immutable class.

from syllable_attempt_1 import Syllable

sounds = {
    # These are for English, with no glottal stop
    "vowels": {"a","e","i","o","u","ɪ","ɛ","ɑ","æ","ʊ","ʌ","ɔ"},
    "consonants": {"b","d","f","g","h","j","k","l","m","n","p","s","t","v","w","z","ʃ","θ","ʒ","ð","ŋ","ɾ","ɹ"},

    "sibilant": {"s","z","ʃ","ʒ"},

    "stop": {"p","t","k","b","d","g"},
    "fricative": {"f","v","θ","ð","s","z","ʃ","ʒ","h"},
    "approximant": {"l","j","w","ɹ"},
    "nasal": {"m","n","ŋ"},

    "voiced": {"b","d","g","j","l","m","n","v","w","z","ʒ","ð","ŋ","ɾ","ɹ"},
    # voiceless = "fghkpstʃθ" I think this can be defined by exclusion

    # These natural classes only apply to consonants
    "natural_classes": {
        "C": "consonants",
        "T": "stop",
        "F": "fricative",
        "S": "sibilant",
        "V": "voiced",  # Not vowel since it's always gonna be in the nucleus
        "R": "approximant",
        "N": "nasal"
    }
}

english_phonemes = {"a","e","i","o","u","ɪ","ɛ","ɑ","æ","ʊ","ʌ","ɔ","b","d","f","g","h","j","k","l","m","n","p","s","t","v","w","z","ʃ","θ","ʒ","ð","ŋ","ɾ|ɹ"},
# add italian_phonemes

# Very not regex-core
# Every phoneme is separated by +
# Order of operations: ~, &, |,
english_onsets = [
    "C~ŋ",
    "T+R~j",
    "~V&F|v+R~j",
    # Figure out the onsets before "u" and reduced forms
    "s+~V&T",
    "s+N~ŋ",
    "s+~V&~S&F"
    "s+m+j"
    "s+f+r"
]

italian_onsets = [
    "C",
    "s+~V&T|f",
    "f|v|T+r",
    "f|v|T&~t&~d+l",
    # "f|v|s|z"
    # Add all the other options
]



def read_onset_possibilities(langauge):
    pass

# Assume this is a real English word, with no syllabic consonants (marked as schwa + consonant)
# Overall broad transcription
# Decomposes the word based on the syllable onset principle
# However, assumes all consecutive vowels are diphthongs
def decompose_word_english(word):
    def check_valid_onset(test_onset):
        letters = test_onset.split("+") # Continue here

        pass


# Consider removing this

# Assume this is a valid input
# Syllable Structure of (C)V(C)
def decompose_word_ex1(word):
    # This code would vary language to language. For now, let's assume always syllables
    # with monophthong vowels, with onsets and codas being at most one consonant but potentially null
    # If there is a consonant between two vowels, it is assumed to be a onset by default
    word += "XXX"
    syllables = []
    while len(word) > 0:
        temp_syllable = ""
        if word[0] == "X":
            break
        if word[0] in consonants:  # Add optional onset
            temp_syllable += word[0]
            word = word[1:]
        temp_syllable += word[0]  # Add nucleus
        word = word[1:]
        # If neither of the following two cases
        # Null coda, next syllable null onset (case 1)
        # Null coda, next syllable non-null onset (case 2)
        if word[0] not in vowels and word[1] not in vowels:
            temp_syllable += word[0]
            word = word[1:]
        syllables.append(temp_syllable.strip("X"))
    return syllables


class Word:
    def __init__(self, word):
        self.original_word = word.lower()
        self.syllables = []
        # Change the type of decompose_word that is used
        for text_syllable in decompose_word_ex1(self.original_word):
            self.syllables.append(Syllable(text_syllable))
        self.num_syllables = len(self.syllables)

    # Kinda janky print but it works ig
    def __str__(self):
        syllable_list = []
        for syllable in self.syllables:
            syllable_list.append(str(syllable))
        return self.original_word + " is " + str(syllable_list).replace("\"", "")


if __name__ == '__main__':
    test_word = Word("testo")
    print(test_word)
