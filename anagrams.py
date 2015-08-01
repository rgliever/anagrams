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
            print("!!! ANAGRAM: %s %s and %s %s"
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
        for w in combo:
            print("%s " %w, end="")
        print("") #newline
        #check the combo for an anagram
        check_anagrams(combo)
        return
    i = start
    while i <= end:
        combo[index] = words[i]
        find_combos(words, combo, k, i+1, end, index+1)
        i += 1

# creates the word array given the rules (removes words <4 characters and
# all punctuation)
def create_word_array(sentence):
    sentence = re.sub('['+punctuation+']', ' ', sentence).lower()
    words = re.sub(r'\b\w{1,3}\b', '', sentence).split()
    return words

def main():
    sentence = "Happy eaters always heat their yappers."
    words = create_word_array(sentence)
    if len(words) < 4:
        print("The sentence does not have enough words more than 3 characters!")
    else:
        k = 4
        combo = [None]*k
        find_combos(words, combo, k, 0, len(words)-1, 0)

main()
