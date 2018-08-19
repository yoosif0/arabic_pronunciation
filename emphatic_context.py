from constants import consonants, emphatics, forwardEmphatics

def getState(letter, nextCharacter):
    emphaticContext = False
    if (letter in consonants + [u'w', u'y'] and not letter in emphatics + [
                    u'r'""", u'l'"""]):  # non-emphatic consonants (except for Lam and Ra) change emphasis back to False
        emphaticContext = False
    if (letter in emphatics):  # Emphatic consonants change emphasis context to True
        emphaticContext = True
    if (nextCharacter in emphatics and not nextCharacter in forwardEmphatics):  # If following letter is backward emphatic, emphasis state is set to True
        emphaticContext = True
    return emphaticContext
