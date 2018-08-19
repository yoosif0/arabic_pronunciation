ArabicScript = {  # mapping from Buckwalter to Arabic script
    u'b': u'\u0628', u'*': u'\u0630', u'T': u'\u0637', u'm': u'\u0645',
    u't': u'\u062a', u'r': u'\u0631', u'Z': u'\u0638', u'n': u'\u0646',
    u'^': u'\u062b', u'z': u'\u0632', u'E': u'\u0639', u'h': u'\u0647',
    u'j': u'\u062c', u's': u'\u0633', u'g': u'\u063a', u'H': u'\u062d',
    u'q': u'\u0642', u'f': u'\u0641', u'x': u'\u062e', u'S': u'\u0635',
    u'$': u'\u0634', u'd': u'\u062f', u'D': u'\u0636', u'k': u'\u0643',
    u'>': u'\u0623', u'\'': u'\u0621', u'}': u'\u0626', u'&': u'\u0624',
    u'<': u'\u0625', u'|': u'\u0622', u'A': u'\u0627', u'Y': u'\u0649',
    u'p': u'\u0629', u'y': u'\u064a', u'l': u'\u0644', u'w': u'\u0648',
    u'F': u'\u064b', u'N': u'\u064c', u'K': u'\u064d', u'a': u'\u064e',
    u'u': u'\u064f', u'i': u'\u0650', u'~': u'\u0651', u'o': u'\u0652'
}




# Convert input string to Arabic
def buckwalterToArabic(word):
    result = u''
    for letter in word:
        if letter in ArabicScript:
            result += ArabicScript[letter]
        else:
            result += letter
    return result
