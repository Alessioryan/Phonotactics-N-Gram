# It's all going to be in here, then I can refactor after
from random import randint

# Storing vowels
# Assumed if not in vowels, in consonants
# CHANGE according to what a language considers a vowel
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

# Global variables
onsets = {""}

# The following maps a string (component) to a list (info) [occurrences, {1: num_occ_1_syllable, 2: num_occ_2...}]
onset_counts = {}
nucleus_counts = {}
coda_counts = {}
# Stores the above in a list for code readability later on
counts = [onset_counts, nucleus_counts, coda_counts]

# Stores the number of words, and syllables, that went into making the onset list and the count
num_words = 0
num_syllables = 0

# Stores the number of onsets, nuclei, and codas
words_syllable_count = {}


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


# Breaks the words into its components and stores their counts in the global variables
def count_word_pieces(file_name):
    # For every word in file, COME BACK TO THIS
    with open(file_name) as file:
        for line in file:
            if line.replace("\n", "") == "":
                continue
            line = clean_line(line)
            for word in line.split(" "):
                syllables = mop_from_s_o_v(separate_on_vowels(word) )
                global num_syllables
                num_syllables += len(syllables)
                length = len(syllables)
                # Store the fact that that word has that number of syllables
                if length not in words_syllable_count:
                    words_syllable_count[length] = 0
                words_syllable_count[length] += 1
                for syllable in syllables:
                    for part in range(3):
                        # Stores the map for the current part of the syllable
                        current_count = counts[part]
                        # Stores the part of the syllable
                        current_syllable_part = syllable[part]
                        # Initialize it if it does not exist, then increment the count by 1
                        if current_syllable_part not in current_count:
                            current_count[current_syllable_part] = [0, {}]
                        current_count[current_syllable_part][0] += 1
                        # Initialize it if it does not exist, then increment the count for that number of syllables by 1
                        if length not in current_count[current_syllable_part][1]:
                            current_count[current_syllable_part][1][length] = 0
                        current_count[current_syllable_part][1][length] += 1


# Parses the onsets and stores them into global variable onsets
def parse_onsets(file_name):
    # For every word in file, COME BACK TO THIS
    with open(file_name) as file:
        for line in file:
            if line.replace("\n", "") == "":
                continue
            line = clean_line(line)
            for word in line.split(" "):
                global num_words
                num_words += 1
                # Identify the coda
                for i in range(len(word)):
                    if word[i] in vowels:
                        # We found the nucleus!
                        onsets.add(word[:i])  # Double check off by one cases
                        break
    file.close()


# Parses the onsets and counts the word pieces
# Note that the count for the number of words is done in parse_onsets
def process(file_name):
    parse_onsets(file_name)
    count_word_pieces(file_name)
    print("Successfully processed " + str(num_words) + " words")


# Generates a random word
def generate_random_word():
    # First, generate a random word length (in syllables)
    random_length_index = randint(1, num_words)
    running_random_length_count = 0
    length = -1
    for key in words_syllable_count:
        running_random_length_count += words_syllable_count[key]
        if random_length_index <= running_random_length_count:
            length = key
            break
    # Then, generate syllables numbering length
    syllables = ""
    for syllable_index in range(length):
        syllable = ""
        for part in range(3):
            # Generate a random onset/nucleus/coda
            random_part_index = randint(1, num_syllables)
            running_random_part_count = 0
            for key in counts[part]:
                running_random_part_count += counts[part][key][0]
                if random_part_index <= running_random_part_count:
                    syllable += key
                    break
        syllables += syllable
    return syllables


# Generates a string of words lengthening parameter
def generate_random_sentence(num):
    sentence = ""
    for word_index in range(num):
        sentence += generate_random_word() + " "
    return sentence.strip(" ")


# Cleans a line
def clean_line(line):
    return line.replace(",", "").replace(".", "").lower().replace("\n", "").replace("'", "").strip(" ")


# Helper testing function
def for_each_word(file_name):
    with open(file_name) as file:
        for line in file:
            if line.replace("\n", "") == "":
                continue
            line = clean_line(line)
            for word in line.split(" "):
                # PUT YOUR TESTING METHOD HERE
                print(mop_from_s_o_v(separate_on_vowels(word) ) )


# Helper assertion method
def assert_correct_sums():
    # Assert the number of words is correct
    expected_words = num_words
    for key in words_syllable_count:
        expected_words -= words_syllable_count[key]
    assert expected_words == 0

    # Assert the number of syllables is correct
    expected_syllables = 0
    # Build up the number of syllables
    for key in words_syllable_count:
        expected_syllables += key * words_syllable_count[key]
    assert expected_syllables == num_syllables
    # Confirm the number of syllables
    for part in range(3):
        expected_part_syllables = expected_syllables
        for part_key in counts[part]:
            expected_part_syllables -= counts[part][part_key][0]
        assert expected_part_syllables == 0

    # Assert the internal counts for each part sums correctly
    for part in range(3):
        for part_key in counts[part]:
            expected_part_key_count = counts[part][part_key][0]
            for part_key_map_key in counts[part][part_key][1]:
                expected_part_key_count -= counts[part][part_key][1][part_key_map_key]
            assert expected_part_key_count == 0


# Helper printing method
def print_all_info():
    print("You have " + str(num_words) + " words saved and " + str(num_syllables) + " syllables saved")
    print("Their syllable counts are " + str(words_syllable_count) )
    print("Allowed onsets are " + str(onsets) )
    print("The onset frequencies:")
    print(onset_counts)
    print("The nucleus frequencies:")
    print(nucleus_counts)
    print("The coda frequencies:")
    print(coda_counts)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # CHANGE THIS FOR DATASET SIZE
    test_set = 10

    if test_set == 0:
        input_file = "lipsum_110.txt"
    elif test_set == 1:
        input_file = "lipsum_454.txt"
    elif test_set == 2:
        input_file = "lipsum_10000.txt"
    elif test_set == 10:
        input_file = "english_2500.txt"
    else:
        input_file = "test.txt"
    process(input_file)
    # print_all_info()
    assert_correct_sums()
    print(generate_random_sentence(100) )
