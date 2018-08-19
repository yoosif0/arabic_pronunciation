#!/usr/bin/python
# -*- coding: UTF8 -*-

import argparse
import os
import re

from arabic_pronunciation import arabic_utils, constants,handle_characters,emphatic_context,remove_duplicates, pronounciations_from_phones, convert_from_arabic_to_phones



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
    elif lastLetter in constants.unambiguousConsonantMap:
        lastLetter = [constants.unambiguousConsonantMap[lastLetter]]
    wordConsonants = re.sub(u'[^h*Ahn\'>wl}kmyTtfdb]', u'', word)  # Remove all dacritics from word
    if wordConsonants in constants.fixedWords:  # check if word is in the fixed word lookup table
        if isinstance(constants.fixedWords[wordConsonants], list):
            done = False
            for pronunciation in constants.fixedWords[wordConsonants]:
                if pronunciation.split(u' ')[-1] in lastLetter:
                    # add each pronunciation to the pronunciation dictionary
                    # results += word + u' ' + pronunciation + u'\n'
                    results += pronunciation + u'\n'
                    pronunciations.append(pronunciation.split(u' '))
                    done = True
            if not done:
                # add each pronunciation to the pronunciation dictionary
                # results += word + u' ' + constants.fixedWords[wordConsonants][0] + u'\n'
                results += constants.fixedWords[wordConsonants][0] + u'\n'
                pronunciations.append(constants.fixedWords[wordConsonants][0].split(u' '))
        else:
            # add pronunciation to the pronunciation dictionary
            # results += word + u' ' + constants.fixedWords[wordConsonants] + u'\n'
            results += constants.fixedWords[wordConsonants] + u'\n'
            pronunciations.append(constants.fixedWords[wordConsonants].split(u' '))
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

        utterance = convert_from_arabic_to_phones.convert(utterance)
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
                word = u'##' + word + u'##'  # This is the end/beginning of word symbol. just for convenience

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
            if letter in constants.unambiguousConsonantMap: 
                phones.append(constants.unambiguousConsonantMap[letter])
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

            if letter in constants.vowelMap:
                # Waw and Ya are complex they could be consonants or vowels and their gemination is complex as
                # it could be a combination of a vowel and consonants
                phones += handle_characters.handle_vowels(previousCharacter, letter, nextCharacter, afterNextCharacter, emphaticContext)
                # Kasra and Damma could be mildened if before a final silent consonant
                if letter in [u'u', u'i']:
                    phones += handle_characters.kasra_and_damma(word, letter, emphaticContext, nextCharacter, afterNextCharacter)
                # Alif could be ommited in definite article and beginning of some words
                if letter in [u'a', u'A', u'Y']:
                    phones += handle_characters.alef(beforePreviousCharacter, previousCharacter, letter, nextCharacter, emphaticContext)
    pronunciations += pronounciations_from_phones.get_different_possible_pronounciations(phones)
    pronunciations = remove_duplicates.remove_duplicates(pronunciations)

    return [' '.join(item) for item in pronunciations if len(item) >=len(arabic_word)]


