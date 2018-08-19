from constants import diacritics, ambiguousConsonantMap, vowelMap, diacritics, maddaMap, unambiguousConsonantMap, diacriticsWithoutShadda, consonants


def lam(beforePreviousCharacter, previousCharacter, nextCharacter, afterNextCharacter):
    if ((not nextCharacter in diacritics and not nextCharacter in vowelMap)
        and afterNextCharacter in [u'~']
        and ((previousCharacter in [u'A', u'l', u'#']) or (
                # Lam could be omitted in definite article (sun letters)
                        previousCharacter in diacritics and beforePreviousCharacter in [u'A', u'l', u'#']))):
        return [ambiguousConsonantMap[u'l'][1]]  # omit
    else:
        return [ambiguousConsonantMap[u'l'][0]]  # do not omit


def alef(beforePreviousCharacter, previousCharacter, letter, nextCharacter, emphaticContext):
    # handle وال  and  كال  but what if this be is fake. TODO
    if letter in [u'A'] and previousCharacter in [u'w', u'k'] and beforePreviousCharacter == u'#' and nextCharacter in [u'l']:
        return [[u'a', vowelMap[letter][0][0]]]
    elif letter in [u'A'] and previousCharacter in [u'u', u'i']:
        return []
    # Waw al jama3a: The Alif after is optional
    elif letter in [u'A'] and previousCharacter in [u'w'] and nextCharacter in [u'#']:
        return [[vowelMap[letter][0][1], vowelMap[letter][0][0]]]
    elif letter in [u'A', u'Y'] and nextCharacter in [u'#']:
        if emphaticContext:
            return [[vowelMap[letter][1][0], vowelMap[u'a'][1]]]
        else:
            return [[vowelMap[letter][0][0], vowelMap[u'a'][0]]]
    else:
        if emphaticContext:
            return [vowelMap[letter][1][0]]
        else:
            return [vowelMap[letter][0][0]]

def p(nextCharacter):
    if (nextCharacter in diacritics):
        return [ambiguousConsonantMap[u'p'][0]]
    else:
        return [ambiguousConsonantMap[u'p'][1]]


def kasra_and_damma(word, letter, emphaticContext, nextCharacter, afterNextCharacter):
    if emphaticContext:
        if ((nextCharacter in unambiguousConsonantMap or nextCharacter == u'l') and afterNextCharacter == u'#' and len(
                word) > 7):
            return [vowelMap[letter][1][1]]
        else:
            return [vowelMap[letter][1][0]]
    else:
        if ((nextCharacter in unambiguousConsonantMap or nextCharacter == u'l') and afterNextCharacter == u'#' and len(
                word) > 7):
            return [vowelMap[letter][0][1]]
        else:
            return [vowelMap[letter][0][0]]


def handle_vowels(previousCharacter, letter, nextCharacter, afterNextCharacter, emphaticContext):
    phones = []
    if (letter in [u'w',u'y']):  # Waw and Ya are complex they could be consonants or vowels and their gemination is complex as it could be a combination of a vowel and consonants
        if (nextCharacter in diacriticsWithoutShadda + [u'A', u'Y'] or (
                        nextCharacter in [u'w', u'y'] and not afterNextCharacter in diacritics + [u'A', u'w',
                                                                                    u'y']) or (
                        previousCharacter in diacriticsWithoutShadda and nextCharacter in consonants + [u'#'])):
            if ((letter in [u'w'] and previousCharacter in [u'u'] and not nextCharacter in [u'a', u'i', u'A',
                                                                                u'Y']) or (
                                letter in [u'y'] and previousCharacter in [u'i'] and not nextCharacter in [u'a',
                                                                                            u'u',
                                                                                            u'A',
                                                                                            u'Y'])):
                if emphaticContext:
                    phones += [vowelMap[letter][1][0]]
                else:
                    phones += [vowelMap[letter][0][0]]
            else:
                if nextCharacter in [u'A'] and letter in [u'w'] and afterNextCharacter in [u'#']:
                    phones += [[vowelMap[letter][0][0], ambiguousConsonantMap[letter]]]
                else:
                    phones += [ambiguousConsonantMap[letter]]
        elif nextCharacter in [u'~']:
            if (previousCharacter in [u'a'] or (letter in [u'w'] and previousCharacter in [u'i', u'y']) or (
                            letter in [u'y'] and previousCharacter in [u'w', u'u'])):
                phones += [ambiguousConsonantMap[letter], ambiguousConsonantMap[letter]]
            else:
                phones += [vowelMap[letter][0][0], ambiguousConsonantMap[letter]]
        else:  # Waws and Ya's at the end of the word could be shortened
            if emphaticContext:
                if (previousCharacter in consonants + [u'u', u'i'] and nextCharacter in [u'#']):
                    phones += [[vowelMap[letter][1][0], vowelMap[letter][1][0][1:]]]
                else:
                    phones += [vowelMap[letter][1][0]]
            else:
                if previousCharacter in consonants + [u'u', u'i'] and nextCharacter in [u'#']:
                    phones += [[vowelMap[letter][0][0], vowelMap[letter][0][0][1:]]]
                else:
                    phones += [vowelMap[letter][0][0]]
    return phones

def madda(emphaticContext):
    if (emphaticContext):
        return [maddaMap[u'|'][1]]
    else:
        return [maddaMap[u'|'][0]]