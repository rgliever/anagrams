from string import punctuation
import re


def check_pair(pairA, pairB):
    return

def check_anagrams(combo):
    pairA = combo[0] + combo[1]
    pairB = combo[2] + combo[3]
    check_pair(pairA, pairB)
    pairA = combo[0] + combo[1]
    pairB = combo[2] + combo[3]
    check_pair(pairA, pairB)
    pairA = combo[0] + combo[1]
    pairB = combo[2] + combo[3]
    check_pair(pairA, pairB)

def find_combos(words, combo, k, start, end, index):
    if index==k:
        #check for anagrams
        for w in combo:
            print("%s " %w, end="")
        print("\n")
        return
    i = start
    while i <= end:
        combo[index] = words[i]
        find_combos(words, combo, k, i+1, end, index+1)
        i += 1

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
