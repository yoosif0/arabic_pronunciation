import re

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


def convert(arabic_word):
    utterance = arabicToBuckwalter(arabic_word)
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

    return utterance
