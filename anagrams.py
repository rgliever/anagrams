# Ryan Gliever, 2015

from string import punctuation
import re

# finds if two strings (which are the concatenation of each pair) are
# anagrams by sorting them and comparing.
# also performs the check for the same word being in both pairs
def check_pair(pairA, pairB):
    if not ((pairA[0] or pairA[1]) == (pairB[0] or pairB[1])):
        stringA = pairA[0] + pairA[1]
        stringB = pairB[0] + pairB[1]
        if len(stringA) == len(stringB) and sorted(stringA) == sorted(stringB):
            print("ANAGRAM: %s %s and %s %s"
            %(pairA[0],pairA[1],pairB[0],pairB[1]))
    return

# checks each possible set of pairs from the combination for anagrams
def check_anagrams(combo):
    pairA = [combo[0], combo[1]]
    pairB = [combo[2], combo[3]]
    check_pair(pairA, pairB)
    pairA = [combo[0], combo[2]]
    pairB = [combo[1], combo[3]]
    check_pair(pairA, pairB)
    pairA = [combo[0], combo[3]]
    pairB = [combo[1], combo[2]]
    check_pair(pairA, pairB)

# recursively finds n choose k combinations of size k.
# in this case n is the number of words in the given text and
# k is 4, since we're seeing if any two words are an anagram of another
# two words
def find_combos(words, combo, k, start, end, index):
    if index==k:
        # one of the combinations
        # check the combo for an anagram
        check_anagrams(combo)
        return
    i = start
    while i <= end:
        combo[index] = words[i]
        find_combos(words, combo, k, i+1, end, index+1)
        i += 1

# creates the word array given the rules (removes words <4 characters and
# all punctuation)
def create_word_array(text):
    text = re.sub('['+punctuation+']', ' ', text).lower()
    words = re.sub(r'\b\w{1,3}\b', '', text).split()
    return words

def main():
    # user input!
    text = "Happy eaters always heat their yappers."
    print("Default text:\n\t" + text)
    user_text = input("Enter some text to check it for anagrams or press "
        + "enter to use the default text:\n")
    if user_text:
        words = create_word_array(user_text)
    else:
        words = create_word_array(text)

    if len(words) < 4:
        print("The text does not have enough words more than 3 characters!")
    else:
        k = 4
        combo = [None]*k
        find_combos(words, combo, k, 0, len(words)-1, 0)

main()
