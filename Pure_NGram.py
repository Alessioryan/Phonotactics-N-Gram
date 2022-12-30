from random import randint


# It's a token!
class NGram:
    def __init__(self, tokens):
        if type(tokens) == type(""):
            tokens = [tokens]
        # Tokens is the tokens of the NGram, whose type is list
        self.tokens = tokens

    def __eq__(self, other):
        if type(self) != type(other):
            raise Exception("Equated different types")
        if len(self.tokens) != len(other.tokens):
            return False
        for index in range(len(self.tokens) ):
            if self.tokens[index] != other.tokens[index]:
                return False
        return True

    def __hash__(self):
        running_string = ""
        for token in self.tokens:
            running_string += token
        return hash(running_string)

    def __str__(self):
        return str(self.tokens)


# Maps the first part of the n-gram to a set with the [total occurances, {ending1: count1, ending2, count2}]
# All strings are wrapped in the NGram class
counts = {}

# The value of the n-gram
n = -1


# Adds the data provided to counts
def add_ngram(ngram):
    start = NGram(ngram[0: n - 1])
    end = NGram(ngram[n - 1])
    if start not in counts:
        counts[start] = [0, {}]
    counts[start][0] += 1
    if end not in counts[start][1]:
        counts[start][1][end] = 0
    counts[start][1][end] += 1


# Parses the words and adds it in count
def parse(file_name):
    # For every word in file, COME BACK TO THIS
    with open(file_name) as file:
        for line in file:
            if line.replace("\n", "") == "":
                continue
            line = clean_line(line)
            line = tokenize(line)
            for i in range(len(line) - n + 1):
                add_ngram(line[i: i + n])
    file.close()


# Processes the input file and sets up a count
def process(file_name, input_n):
    if input_n > 4 or input_n < 2:
        raise Exception("Invalid n, currently only 2 <= n <= 4 supported")
    global n
    n = input_n
    parse(file_name)


# Generates a random character given the n-1-gram provided
# Takes a string, returns a string
def generate_from_n_minus_1(n_minus_1):
    n_minus_1_gram = NGram(n_minus_1)
    random_count = randint(1, counts[n_minus_1_gram][0])
    running_count = 0
    for ending in counts[n_minus_1_gram][1]:
        running_count += counts[n_minus_1_gram][1][ending]
        if running_count >= random_count:
            return ending.tokens[0]
    raise Exception("Generation issue")


# Generates a random word, starting with " " and ending with " ". Strips " ".
def generate_random_word():
    if n == 2:
        running_string = ["<s>"]
    elif n == 3:
        running_string = ["< >", "<s>"]
    elif n == 4:
        running_string = ["</s>", "< >", "<s>"]
    while running_string[-1] != "</s>":
        n_minus_1 = []
        for i in range(n - 1):
            n_minus_1.append(running_string[len(running_string) - n + 1 + i] )
        running_string.append(generate_from_n_minus_1(n_minus_1) )  # Update accordingly when fitting for n > 2
    return "".join(running_string).replace("<s>","").replace("</s>","").replace("< >","")


# Generates a string of words lengthening parameter
def generate_random_sentence(num):
    sentence = ""
    for word_index in range(num):
        sentence += generate_random_word() + " "
    return sentence.strip(" ")


# Cleans a line
def clean_line(line):
    return " " + line.replace(",", "").replace(".", "").lower().replace("\n", "").replace("'", "").strip(" ") + " "


# Tokenizes a sentence according to token type, returns an array of strings
def tokenize(line):
    array = []
    for index in range(len(line)):
        if line[index] == ' ':
            array.append("</s>")
            array.append("< >")
            array.append("<s>")
        else:
            array.append(line[index])
    return array


# Prints all data collected
def print_all_data():
    print()
    print("Models are built on a " + str(n) + "gram")
    for key in counts:
        print("Given " + str(key) + ": , which appears " + str(counts[key][0]) + " times")
        running_string = ""
        for end in counts[key][1]:
            running_string += "{" + str(end) + ": " + str(counts[key][1][end]) + "}, "
        print(running_string.strip(" ") )
    print()


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

    process(input_file, 4)
    print_all_data()
    print(generate_random_sentence(100) )
