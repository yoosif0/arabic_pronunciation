import argparse
import operator
import re
import collections

import phonetise_Arabic
from arutils import arabic_utils

parser = argparse.ArgumentParser(description='extracts dictionary and phones from a corpus')
parser.add_argument('-i', '--input', type=argparse.FileType(mode='r', encoding='utf-8'),
                    help='input file', required=True)
parser.add_argument('-p', '--project-name', type=str,
                    help='project name', required=True)
parser.add_argument('-s', '--s-tag', action='store_true',
                    help='the sentences include <s> tag')


def calculateFrequencies(dic):
    for word in dic:
        dic[word]=collections.Counter(dic[word])

def corpus2dictionary(corpus, project_name):
    pronunciation_dict = {}
    pronunciation_dict_cleaned={}
    phones_list = set()
    phones_list.add('SIL')
    for line in corpus:
        if args.s_tag:
            sentence = re.search('<s>(.*)</s>', line).group(1)
        else:
            sentence = line
        words = sentence.split()
        for word in words:
            pronunciations = phonetise_Arabic.phonetise_word(word)
            for pronunciation in pronunciations:
                for phone in pronunciation.split():
                    phones_list.add(phone)

            def addWordToDictionary(localWord, dic):
                if localWord not in dic:
                    dic[localWord] = []
                dic[localWord].extend(pronunciations)
            cleaned_word = arabic_utils.remove_diacritics(word)
            addWordToDictionary(word, pronunciation_dict)
            addWordToDictionary(cleaned_word, pronunciation_dict_cleaned)

    calculateFrequencies(pronunciation_dict)
    calculateFrequencies(pronunciation_dict_cleaned)

    print('writing 2 dic files')
    writeFile(pronunciation_dict, proj_name + '_moshakal.dic')
    writeFile(pronunciation_dict_cleaned, proj_name + '_cleaned.dic')

    print('writing phone file')
    with open(proj_name + '.phone', mode='w', encoding='utf-8') as phone_writer:
        for ph in sorted(phones_list):
            phone_writer.write(ph)
            phone_writer.write('\n')


def writeFile(dic, fileName):
    with open(fileName, mode='w', encoding='utf-8') as dict_writer:
        for w, phones in sorted(dic.items()):
            for k,v in phones.most_common():
                dict_writer.write('{}\t\t{}\t\t{}\n'.format(w, k,v))

if __name__ == '__main__':
    args = parser.parse_args()
    corpus = args.input.readlines()
    proj_name = args.project_name
    corpus2dictionary(corpus, project_name=proj_name)
