# It's all going to be in here, then I can refactor after

# Storing vowels
# Assumed if not in vowels, in consonants
vowels = {'a', 'e', 'i', 'o', 'u'}

# Global variables
onsets = {""}

# The following maps a string (component) to a list (info) [occurances, [occ. 1 syllable, occ. 2 syllable, ...]]
onset_counts = {}
nucleus_counts = {}
coda_counts = {}


# Returns a list separated on its vowels, referred to as s_o_v
def separate_on_vowels(word):
    # Odd indices are C, even are V
    c_v_segments = []
    for letter in word:
        if letter in vowels:
            # VOWELS
            # If last one is a vowel, add null consonant
            if len(c_v_segments) % 2 == 0:
                c_v_segments.append("")
            c_v_segments.append(letter)
        else:
            # CONSONANTS
            # If last one is a vowel, add the consonant
            if len(c_v_segments) % 2 == 0:
                c_v_segments.append(letter)
            else:
                c_v_segments[-1] = c_v_segments[-1] + letter
    # Must check to see if last part is a vowel, if it is, add a ""
    if c_v_segments[-1] in vowels:
        c_v_segments.append("")
    return c_v_segments


# Return a list of syllables based on the maximal onset principle,
# where each syllable is a 3 part list of onset, nucleus, and coda
# For now, ASSUME that the first syllable onset in onsets
# For now, ASSUME that all language allow for null onset
def mop_from_s_o_v(s_o_v):
    print("THIS s_o_v is " + str(s_o_v) )
    syllables = []
    while len(s_o_v) != 0:
        if len(s_o_v) == 1:
            # This is just an onset then
            # If we have a good understanding of all possible onsets, it should in theory be an empty string
            if s_o_v[0] == "":
                return syllables
            else:
                raise Exception("Should be empty string")
        else:  # Length of s_o_v will always be odd
            assert len(s_o_v) % 2 == 1
            syllable = []
            # Add the nucleus and coda
            syllable.insert(0, s_o_v[-1])  # Coda
            s_o_v.pop(-1)
            syllable.insert(0, s_o_v[-1])  # Nucleus
            s_o_v.pop(-1)
            # Find the maximal onset
            coda_onset = s_o_v[-1]
            num_onset = len(coda_onset)
            while num_onset >= 0:
                if coda_onset[len(coda_onset) - num_onset:] in onsets:
                    break
                num_onset -= 1
            # Sanity check, might misfire if "" not in onsets
            assert num_onset != -1
            # Now, we have found the biggest onset
            # We insert it into syllable in onset position
            syllable.insert(0, coda_onset[len(coda_onset) - num_onset:] )
            # We modify s_o_v, removing the onset
            s_o_v[-1] = coda_onset[:len(coda_onset) - num_onset]
            syllables.insert(0, syllable)


# Breaks the words into its components,
def count_word_pieces(file_name):
    # For every word in file, COME BACK TO THIS
    with open(file_name) as file:
        while True:
            line = file.readline().replace(",", "").replace(".", "").lower().replace("\n", "")
            if line == "":
                break
            for word in line.split(" "):
                print(separate_on_vowels(word))
                # vowel_breaks = separate_on_vowels(word)


# Parses the onsets and stores them into global variable onsets
def parse_onsets(file_name):
    # For every word in file, COME BACK TO THIS
    with open(file_name) as file:
        while True:
            line = file.readline().replace(",", "").replace(".", "").lower().replace("\n", "")
            if line == "":
                break
            for word in line.split(" "):
                # Identify the coda
                for i in range(len(word)):
                    if word[i] in vowels:
                        # We found the nucleus!
                        onsets.add(word[:i])  # Double check off by one cases
                        break


# Helper testing function
def for_each_word(file_name):
    with open(file_name) as file:
        while True:
            line = file.readline().replace(",", "").replace(".", "").lower().replace("\n", "")
            if line == "":
                break
            for word in line.split(" "):
                # PUT YOUR TESTING METHOD HERE
                print(mop_from_s_o_v(separate_on_vowels(word) ) )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # CHANGE THIS FOR DATASET SIZE
    test_set = 2

    if test_set == 0:
        input_file = "lipsum_110.txt"
    elif test_set == 1:
        input_file = "lipsum_454.txt"
    elif test_set == 2:
        input_file = "lipsum_10000.txt"
    else:
        input_file = "test.txt"
    parse_onsets(input_file)
    print(onsets)
    for_each_word(input_file)
    # count_word_pieces("lipsum_10000.txt")
