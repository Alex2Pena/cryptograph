# imports the natural talk library
import nltk
# downloads the 'words' portion of the library
nltk.download('words', quiet=True)
# downloads the 'names' portion of the library
nltk.download('names', quiet=True)
# downloads the 'wordnet' portion of the library
nltk.download('wordnet', quiet=True)

# imports once downloaded
from nltk.corpus import words, names, wordnet

word_list = words.words()
name_list = names.words()
wordnet_list = wordnet.words()

# print(word_list[0:5000])
