def remove_duplicates(pronunciations):
    for pronunciation in pronunciations:
        prevLetter = u''
        toDelete = []
        for i in range(0, len(pronunciation)):
            letter = pronunciation[i]
            # Delete duplicate consecutive vowels
            if (letter in [u'aa', u'uu0', u'ii0', u'AA', u'UU0', u'II0'] and prevLetter.lower() == letter[
                                                                                                   1:].lower()):
                toDelete.append(i - 1)
                pronunciation[i] = pronunciation[i - 1][0] + pronunciation[i - 1]
            if letter in [u'u0', u'i0'] and prevLetter.lower() == letter.lower():  # Delete duplicates
                toDelete.append(i - 1)
                pronunciation[i] = pronunciation[i - 1]
            if letter in [u'y', u'w'] and prevLetter == letter:  # delete duplicate
                pronunciation[i - 1] += pronunciation[i - 1]
                toDelete.append(i)
            if letter in [u'a'] and prevLetter == letter:  # delete duplicate
                toDelete.append(i)

            prevLetter = letter
        for i in reversed(range(0, len(toDelete))):
            del (pronunciation[toDelete[i]])
    return pronunciations