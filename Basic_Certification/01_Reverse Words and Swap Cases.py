#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    words_in_sentence = sentence.split()
    words_in_sentence = list(reversed(words_in_sentence))
    reversed_swapped_sentence = " ".join(words_in_sentence)
    return reversed_swapped_sentence.swapcase()

if __name__ == '__main__':
    sentence = input()
    result = reverse_words_order_and_swap_cases(sentence)
    print(result + '\n')