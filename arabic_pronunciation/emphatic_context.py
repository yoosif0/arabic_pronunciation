from arabic_pronunciation.constants import consonants, emphatics, forwardEmphatics

def getState(letter, nextCharacter):
    emphaticContext = False
    if (letter in consonants + [u'w', u'y'] and not letter in emphatics + [ u'r', u'l']):
        emphaticContext = False
    if (letter in emphatics):  # Emphatic consonants change emphasis context to True
        emphaticContext = True
    if (nextCharacter in emphatics and not nextCharacter in forwardEmphatics):  # If following letter is backward emphatic, emphasis state is set to True
        emphaticContext = True
    return emphaticContext
