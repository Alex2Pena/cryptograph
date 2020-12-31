# imports the dictionary/corpus/word_list from the corpus loader
from corpus_loader import word_list, name_list, wordnet_list
import re


def count_words(text):
    master_wordlist = word_list + name_list
    input_words = text.split()
    word_count = 0

    for each_word in input_words:
        maybe_word = re.sub(r'[^A-Za-z]+', '', each_word)
        if maybe_word.lower() in master_wordlist:
            word_count += 1
    print(word_count, " English words detected")
    print(word_count / len(input_words), " of original input is english")
    return word_count


count_words('Only names and words here ')
