import re
from constants import unambiguousConsonantMap, fixedWords

# modification in isFixedWord2 is just to return the pronunciations without the word
def isFixedWord2(word):
    pronunciations = []
    lastLetter = ''
    if len(word) > 0:
        lastLetter = word[-1]
    if lastLetter == u'a':
        lastLetter = [u'a', u'A']
    elif lastLetter == u'A':
        lastLetter = [u'aa']
    elif lastLetter == u'u':
        lastLetter = [u'u0']
    elif lastLetter == u'i':
        lastLetter = [u'i0']
    elif lastLetter in unambiguousConsonantMap:
        lastLetter = [unambiguousConsonantMap[lastLetter]]
    wordConsonants = re.sub(u'[^h*Ahn\'>wl}kmyTtfdb]', u'', word)  # Remove all dacritics from word
    if wordConsonants in fixedWords:  # check if word is in the fixed word lookup table
        if isinstance(fixedWords[wordConsonants], list):
            done = False
            for pronunciation in fixedWords[wordConsonants]:
                if pronunciation.split(u' ')[-1] in lastLetter:
                    pronunciations.append(pronunciation.split(u' '))
                    done = True
            if not done:
                pronunciations.append(fixedWords[wordConsonants][0].split(u' '))
        else:
            pronunciations.append(fixedWords[wordConsonants].split(u' '))
    return pronunciations