Overview of how the program will work

MOP_Independent_Components:
1. Parse a LARGE set of words as found naturally in a language
    ASSUME a. Orthography corresponds directly to phonetic reading
           b. Input is written in IPA
2. Iterate once, finding all onsets
    ASSUME Only vowel nuclei
    ASSUME Only monophthongs (for now)
3. Iterate again, decomposing words into syllables and counting frequency


Pure_NGram:
1. A complete NGram model from scratch