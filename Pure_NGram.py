
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
    if end not in counts[start]:
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


# Cleans a line
def clean_line(line):
    return " " + line.replace(",", "").replace(".", "").lower().replace("\n", "").replace("'", "").strip(" ") + " "


# Prints all data collected
def print_all_data():
    print("Models are built on a " + str(n) + "gram")
    print(counts)
    for key in counts:
        print("Given " + key + ": " + str(counts[key]) )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # CHANGE THIS FOR DATASET SIZE
    test_set = -1

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