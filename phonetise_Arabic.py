#!/usr/bin/python
# -*- coding: UTF8 -*-

import argparse
import os
import re

import findstress
from arutils import arabic_utils
from constants import *
import handle_characters
import emphatic_context
from remove_duplicates import remove_duplicates
from pronounciations_from_phones import get_different_possible_pronounciations
buckwalter = {  # mapping from Arabic script to Buckwalter
    u'\u0628': u'b', u'\u0630': u'*', u'\u0637': u'T', u'\u0645': u'm',
    u'\u062a': u't', u'\u0631': u'r', u'\u0638': u'Z', u'\u0646': u'n',
    u'\u062b': u'^', u'\u0632': u'z', u'\u0639': u'E', u'\u0647': u'h',
    u'\u062c': u'j', u'\u0633': u's', u'\u063a': u'g', u'\u062d': u'H',
    u'\u0642': u'q', u'\u0641': u'f', u'\u062e': u'x', u'\u0635': u'S',
    u'\u0634': u'$', u'\u062f': u'd', u'\u0636': u'D', u'\u0643': u'k',
    u'\u0623': u'>', u'\u0621': u'\'', u'\u0626': u'}', u'\u0624': u'&',
    u'\u0625': u'<', u'\u0622': u'|', u'\u0627': u'A', u'\u0649': u'Y',
    u'\u0629': u'p', u'\u064a': u'y', u'\u0644': u'l', u'\u0648': u'w',
    u'\u064b': u'F', u'\u064c': u'N', u'\u064d': u'K', u'\u064e': u'a',
    u'\u064f': u'u', u'\u0650': u'i', u'\u0651': u'~', u'\u0652': u'o'
}

# Convert input string to Buckwalter
def arabicToBuckwalter(word):
    result = u''
    for letter in word:
        if letter in buckwalter:
            result += buckwalter[letter]
        else:
            result += letter
    return result


def isFixedWord(word, results, orthography, pronunciations):
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
                    results += word + u' ' + pronunciation + u'\n'  # add each pronunciation to the pronunciation dictionary
                    pronunciations.append(pronunciation.split(u' '))
                    done = True
            if not done:
                # add each pronunciation to the pronunciation dictionary
                results += word + u' ' + fixedWords[wordConsonants][0] + u'\n'
                pronunciations.append(fixedWords[wordConsonants][0].split(u' '))
        else:
            # add pronunciation to the pronunciation dictionary
            results += word + u' ' + fixedWords[wordConsonants] + u'\n'
            pronunciations.append(fixedWords[wordConsonants].split(u' '))
    return results


# modification in isFixedWord2 is just to return the pronunciations without the word
def isFixedWord2(word, results, orthography, pronunciations):
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
                    # add each pronunciation to the pronunciation dictionary
                    # results += word + u' ' + pronunciation + u'\n'
                    results += pronunciation + u'\n'
                    pronunciations.append(pronunciation.split(u' '))
                    done = True
            if not done:
                # add each pronunciation to the pronunciation dictionary
                # results += word + u' ' + fixedWords[wordConsonants][0] + u'\n'
                results += fixedWords[wordConsonants][0] + u'\n'
                pronunciations.append(fixedWords[wordConsonants][0].split(u' '))
        else:
            # add pronunciation to the pronunciation dictionary
            # results += word + u' ' + fixedWords[wordConsonants] + u'\n'
            results += fixedWords[wordConsonants] + u'\n'
            pronunciations.append(fixedWords[wordConsonants].split(u' '))
    return results




def phonetise_word(arabic_word):
    utterances = [arabic_word]
    arabic_word = arabic_utils.remove_diacritics(arabic_word)
    result = ''  # Pronunciations Dictionary
    utterances_pronunciations = []  # Most likely pronunciation for all utterances
    utterances_pronunciations_with_boundaries = []  # Most likely pronunciation for all utterances
    pronunciations=[]
    phones=[]
    # -----------------------------------------------------------------------------------------------------
    # Loop through utterances------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------
    utterance_number = 1
    for utterance in utterances:
        utterance_number += 1
        utterances_pronunciations.append('')  # Add empty entry that will hold this utterance's pronuncation
        # Add empty entry that will hold this utterance's pronuncation
        utterances_pronunciations_with_boundaries.append('')

        utterance = arabicToBuckwalter(utterance)
        # print(u"phoetising utterance")
        # print(utterance)
        # Do some normalisation work and split utterance to words
        utterance = utterance.replace(u'AF', u'F')
        utterance = utterance.replace(u'\u0640', u'')
        utterance = utterance.replace(u'o', u'')
        utterance = utterance.replace(u'aA', u'A')
        utterance = utterance.replace(u'aY', u'Y')
        utterance = re.sub(u'([^\\-]) A', u'\\1 ', utterance)
        utterance = utterance.replace(u'F', u'an')
        utterance = utterance.replace(u'N', u'un')
        utterance = utterance.replace(u'K', u'in')
        utterance = utterance.replace(u'|', u'>A')

        # Deal with Hamza types that when not followed by a short vowel letter,
        # this short vowel is added automatically
        utterance = re.sub(u'^Ai', u'<i', utterance)
        utterance = re.sub(u'^Aa', u'>a', utterance)
        utterance = re.sub(u'^Au', u'>u', utterance)
        utterance = re.sub(u'Ai', u'<i', utterance)
        utterance = re.sub(u'Aa', u'>a', utterance)
        utterance = re.sub(u'Au', u'>u', utterance)
        utterance = re.sub(u'^Al', u'>al', utterance)
        utterance = re.sub(u' - Al', u' - >al', utterance)
        utterance = re.sub(u'^- Al', u'- >al', utterance)
        utterance = re.sub(u'^>([^auAw])', u'>a\\1', utterance)
        utterance = re.sub(u' >([^auAw ])', u' >a\\1', utterance)
        utterance = re.sub(u'<([^i])', u'<i\\1', utterance)
        utterance = re.sub(u' A([^aui])', u' \\1', utterance)
        utterance = re.sub(u'^A([^aui])', u'\\1', utterance)

        utterance = utterance.split(u' ')
        # ---------------------------
        word_index = -1

        # Loop through words
        for word in utterance:
            word_index += 1
            if word not in [u'-', u'sil']:
                pronunciations = []  # Start with empty set of possible pronunciations of current word
                # Add fixed irregular pronunciations if possible
                result = isFixedWord2(word, result, word, pronunciations)
                # Indicates whether current character is in an emphatic context or not. Starts with False
                emphaticContext = False
                word = u'bb' + word + u'ee'  # This is the end/beginning of word symbol. just for convenience

                phones = []  # Empty list which will hold individual possible word's pronunciation

                # -----------------------------------------------------------------------------------
                # MAIN LOOP: here is where the Modern Standard Arabic phonetisation rule-set starts--
                # -----------------------------------------------------------------------------------
        # MAIN LOOP: here is where the Modern Standard Arabic phonetisation rule-set starts--
        # -----------------------------------------------------------------------------------
        for index in range(2, len(word) - 2):
            letter = word[index]  # Current Character
            nextCharacter = word[index + 1]  # Next Character
            afterNextCharacter = word[index + 2]  # Next-Next Character
            previousCharacter = word[index - 1]  # Previous Character
            beforePreviousCharacter = word[index - 2]  # Before Previous Character
            emphaticContext = emphatic_context.getState(letter, nextCharacter)
            if letter in unambiguousConsonantMap: 
                phones.append(unambiguousConsonantMap[letter])
            # ----------------------------------------------------------------------------------------------------------------
            if letter == u'l':  # Lam is a consonant which requires special treatment
                phones += handle_characters.lam(beforePreviousCharacter, previousCharacter, nextCharacter, afterNextCharacter)
            # ----------------------------------------------------------------------------------------------------------------
            # shadda just doubles the letter before it
            if letter == u'~' and previousCharacter not in [u'w', u'y'] and len(phones) > 0:
                phones[-1] += phones[-1]
            # ----------------------------------------------------------------------------------------------------------------
            if letter == u'|':  # Madda only changes based in emphaticness
                phones += handle_characters.madda(emphatic_context)
            # ----------------------------------------------------------------------------------------------------------------
            if letter == u'p':  # Ta' marboota is determined by the following if it is a diacritic or not
                phones += handle_characters.p(nextCharacter)

            if letter in vowelMap:
                # Waw and Ya are complex they could be consonants or vowels and their gemination is complex as
                # it could be a combination of a vowel and consonants
                phones += handle_characters.handle_vowels(previousCharacter, letter, nextCharacter, afterNextCharacter, emphaticContext)
                # Kasra and Damma could be mildened if before a final silent consonant
                if letter in [u'u', u'i']:
                    phones += handle_characters.kasra_and_damma(word, letter, emphaticContext, nextCharacter, afterNextCharacter)
                # Alif could be ommited in definite article and beginning of some words
                if letter in [u'a', u'A', u'Y']:
                    phones += handle_characters.alef(beforePreviousCharacter, previousCharacter, letter, nextCharacter, emphaticContext)
    pronunciations += get_different_possible_pronounciations(phones)
    pronunciations = remove_duplicates(pronunciations)

    return [' '.join(item) for item in pronunciations if len(item) >=len(arabic_word)]

# -----------------------------------------------------------------------------------------------------
# Read input file--------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------


parser = argparse.ArgumentParser(description='extracts dictionary and phones from a corpus')
parser.add_argument('-i', '--input', type=argparse.FileType(mode='r', encoding='utf-8'),
                    help='input file', required=True)

