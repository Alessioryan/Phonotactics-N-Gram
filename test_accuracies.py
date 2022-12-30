
# The dictionary with all words considered to be real
dicc = set()


# Parses the dictionary file and adds all words to the dictionary
def parse_dictionary(file_name):
    global dicc
    # For every word in file, COME BACK TO THIS
    with open(file_name) as file:
        for line in file:
            line = line.replace("\n", "")
            if line == "":
                continue
            for word in line.split(" "):
                dicc.add(word)
    print(dicc)
    file.close()


# Tests the accuracy given the words in words
def test_accuracy(words):
    count = 0
    hits = 0
    for word in words.split(" "):
        count += 1
        if word in dicc:
            hits += 1
    return hits / count


# Press the green button to test your words!
if __name__ == '__main__':
    dictionary = 0
    words = "yielding even first one deeping him third brought to morning givenish wont youll shale upon togeth behold shall divided bring you first be sea fly have days morninged thered void firmament creature light ther sixth creater second whall water beginning therein place open life bear oure god fowl his fly yielding bearth bear wing yourth kind livided divided wont mover deeping multiply heave thing life fish heave males thing you appearing grass signs man firmament fruit be moveth a own land behold and theyre even spirit fill thing over heaven yearth whering kind fruit place fowl even night lights dominion"

    if dictionary == 0:
        dictionary_file = 'mainDicc.txt'
    else:
        pass

    parse_dictionary(dictionary_file)
    accuracy = test_accuracy(words)
    print(accuracy)