"""
File: anagram.py
Name: Tracy Lee
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This program recursively finds all the anagram(s)
    for the word input by user and terminates when the
    input string matches the EXIT constant defined
    at line 19.
    """
    print("Welcome to stanCode \"Anagram Generator\"(or -1 to quit)")
    while True:
        anagram = input("Find anagram for: ")
        if anagram == EXIT:
            break
        start = time.time()
        find_anagrams(anagram)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    """
    :param s: str; The target word.
    :return: list; The list stores all words that match the target number of letters.

    The program will find words from the dictionary
    that have the same number of words as the target word and store them in a python list.
    """
    word_list = []
    with open(FILE, "r") as f:
        for line in f:
            word = line.strip()
            if len(s) == len(word):
                word_list.append(word)
    return word_list


def find_anagrams(s):
    """
    :param s: str; The target word.
    :return: list; The list of all anagrams.

    This function will print all anagrams in the dictionary.
    """
    dictionary_list = read_dictionary(s)
    anagram_list = []
    find_anagrams_helper(s, "", dictionary_list, anagram_list)
    print(f"{len(anagram_list)} anagrams: {anagram_list}")


def find_anagrams_helper(s, ans, lst, ana_list):
    """
    :param s: str; The target word.
    :param ans: str; Other words with the same letter combination as the target word.
    :param lst: list; The list stores all words that match the target number of letters.
    :param ana_list: list; The list of all found words.
    :return ans: str; Other words with the same letter combination as the target word.
    :return ana_list: list; The list of all anagrams.

    The helper function will find the anagram in the lst.
    And store all anagrams in ana_list.
    """
    if len(ans) == len(s) and ans in lst and ans not in ana_list:
        print("Searching...")
        print("Found: " + ans)
        ana_list.append(ans)
    else:
        for alphabet in s:
            # choose
            ans += alphabet
            if ans.count(alphabet) <= s.count(alphabet) and has_prefix(ans, lst):
                # explore
                find_anagrams_helper(s, ans, lst, ana_list)
            # un-choose
            ans = ans[:-1]


def has_prefix(sub_s, lst):
    """
    :param sub_s: str; The string consisting of the letters of the target word.
    :param lst: list; The list stores all words that match the target number of letters.
    :return: bool; If there is a word in lst starts with sub_s, return True. Otherwise, return False.
    ---------------------------
    The program will check if the word starts with sub_s.
    If there is a word in lst starts with sub_s, return True. Otherwise, return False.
    """
    for word in lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
