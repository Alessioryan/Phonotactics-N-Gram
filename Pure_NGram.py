
from random import randint

# Maps the first part of the n-gram to a set with the [total occurances, {ending1: count1, ending2, count2}]
counts = {}

# The value of the n-gram
n = -1


# Adds the data provided to counts
def add_ngram(ngram):
    start = ngram[0 : n-1]
    end = ngram[n-1]
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
            for i in range(len(line) - n + 1):
                add_ngram(line[i: i + n])
    file.close()


# Processes the input file and sets up a count
def process(file_name, input_n):
    global n
    n = input_n
    parse(file_name)


# Generates a random character given the n-1-gram provided
def generate_n_minus_1_gram(n_minus_1_gram):
    random_count = randint(1, counts[n_minus_1_gram][0])
    running_count = 0
    for ending in counts[n_minus_1_gram][1]:
        running_count += counts[n_minus_1_gram][1][ending]
        if running_count >= random_count:
            return ending
    raise Exception("Generation issue")


# Generates a random word, starting with " " and ending with " ". Strips " ".
def generate_random_word():
    running_string = " " + generate_n_minus_1_gram(" ")
    while running_string[-1] != ' ':
        running_string += generate_n_minus_1_gram(running_string[-1] ) # Update accordingly when fitting for n > 2
    return running_string.strip(" ")


# Generates a string of words lengthening parameter
def generate_random_sentence(num):
    sentence = ""
    for word_index in range(num):
        sentence += generate_random_word() + " "
    return sentence.strip(" ")


# Cleans a line
def clean_line(line):
    return " " + line.replace(",", "").replace(".", "").lower().replace("\n", "").replace("'", "").strip(" ") + " "


# Prints all data collected
def print_all_data():
    print()
    print("Models are built on a " + str(n) + "gram")
    print(counts)
    for key in counts:
        print("Given " + key + ": " + str(counts[key]) )
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

    process(input_file, 2)
    print_all_data()
    print(generate_random_sentence(100) )
