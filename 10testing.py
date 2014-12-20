#10testing.py
#!/usr/bin/python

import locale
import sys

def count_words(str):

    word_count = 0
    in_word = False
    for c in str:
        if in_word and not c.isalnum():
            in_word = False
        elif not in_word and c.isalnum():
            in_word = True
            word_count += 1
    return word_count

def main():
    locale.setlocale(locale.LC_ALL, "")

    line_count = 0
    word_count = 0
    char_count = 0

    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.decode(locale.getpreferredencoding())
        char_count += len(line)
        line_count += 1
        word_count += count_words(line)

    sys.stdout.write("%d words, %d lines, %d chars\n" %
                     (word_count, line_count, char_count))

main()