#!/usr/bin/python

import sys

files = list(sys.argv)
files.pop(0)
# print('files:', files)

input = input("Enter the word you want to search for: ")
# print('input:', input)

def readFromFile(fileName):
    lines = list(open(fileName, 'r'))
    lineCount = 0
    found = False

    for line in lines:
        lineCount += 1
        wordCount = 0

        words = line.split(' ')

        for word in words:
            wordCount += 1

            if word[-1] == ',' or word[-1] == '.':
                word = word[:-1]

            if word.lower() == input.lower():
                print(fileName, '\t', lineCount, '\t\t', wordCount, '\t\t', word, sep = '')
                found = True

    if not found:
        print(fileName, '\tN/A\t\tN/A\t\t', input, sep = '')

print('File Name\tLine Number\tWord Number\tWord')

for file in files:
    readFromFile(file)
