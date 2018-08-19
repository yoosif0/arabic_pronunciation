unambiguousConsonantMap = {
    u'b': u'b', u'*': u'*', u'T': u'T', u'm': u'm',
    u't': u't', u'r': u'r', u'Z': u'Z', u'n': u'n',
    u'^': u'^', u'z': u'z', u'E': u'E', u'h': u'h',
    u'j': u'j', u's': u's', u'g': u'g', u'H': u'H',
    u'q': u'q', u'f': u'f', u'x': u'x', u'S': u'S',
    u'$': u'$', u'd': u'd', u'D': u'D', u'k': u'k',
    u'>': u'<', u'\'': u'<', u'}': u'<', u'&': u'<',
    u'<': u'<'
}

ambiguousConsonantMap = {
    u'l': [u'l', u''], u'w': u'w', u'y': u'y', u'p': [u't', u'']
    # These consonants are only unambiguous in certain contexts
}

maddaMap = {
    u'|': [[u'<', u'aa'], [u'<', u'AA']]
}

vowelMap = {
    u'A': [[u'aa', u''], [u'AA', u'']], u'Y': [[u'aa', u''], [u'AA', u'']],
    u'w': [[u'uu0', u'uu1'], [u'UU0', u'UU1']],
    u'y': [[u'ii0', u'ii1'], [u'II0', u'II1']],
    u'a': [u'a', u'A'],
    u'u': [[u'u0', u'u1'], [u'U0', u'U1']],
    u'i': [[u'i0', u'i1'], [u'I0', u'I1']],
}

nunationMap = {
    u'F': [[u'a', u'n'], [u'A', u'n']], u'N': [[u'u1', u'n'], [u'U1', u'n']], u'K': [[u'i1', u'n'], [u'I1', u'n']]
}

diacritics = [u'o', u'a', u'u', u'i', u'F', u'N', u'K', u'~']
diacriticsWithoutShadda = [u'o', u'a', u'u', u'i', u'F', u'N', u'K']
emphatics = [u'D', u'S', u'T', u'Z', u'g', u'x', u'q']
forwardEmphatics = [u'g', u'x']
consonants = [u'>', u'<', u'}', u'&', u'\'', u'b', u't', u'^', u'j', u'H', u'x', u'd', u'*', u'r', u'z', u's', u'$',
              u'S', u'D', u'T', u'Z', u'E', u'g', u'f', u'q', u'k', u'l', u'm', u'n', u'h', u'|']

# ------------------------------------------------------------------------------------
# Words with fixed irregular pronunciations-------------------------------------------
# ------------------------------------------------------------------------------------
fixedWords = {
    u'h*A': [u'h aa * aa', u'h aa * a', ],
    u'bh*A': [u'b i0 h aa * aa', u'b i0 h aa * a', ],
    u'kh*A': [u'k a h aa * aa', u'k a h aa * a', ],
    u'fh*A': [u'f a h aa * aa', u'f a h aa * a', ],
    u'h*h': [u'h aa * i0 h i0', u'h aa * i1 h'],
    u'bh*h': [u'b i0 h aa * i0 h i0', u'b i0 h aa * i1 h'],
    u'kh*h': [u'k a h aa * i0 h i0', u'k a h aa * i1 h'],
    u'fh*h': [u'f a h aa * i0 h i0', u'f a h aa * i1 h'],
    u'h*An': [u'h aa * aa n i0', u'h aa * aa n'],
    u'h&lA\'': [u'h aa < u0 l aa < i0', u'h aa < u0 l aa <'],
    u'*lk': [u'* aa l i0 k a', u'* aa l i0 k'],
    u'b*lk': [u'b i0 * aa l i0 k a', u'b i0 * aa l i0 k'],
    u'k*lk': [u'k a * aa l i0 k a', u'k a * aa l i1 k'],
    u'*lkm': u'* aa l i0 k u1 m',
    u'>wl}k': [u'< u0 l aa < i0 k a', u'< u0 l aa < i1 k'],
    u'Th': u'T aa h a',
    u'lkn': [u'l aa k i0 nn a', u'l aa k i1 n'],
    u'lknh': u'l aa k i0 nn a h u0',
    u'lknhm': u'l aa k i0 nn a h u1 m',
    u'lknk': [u'l aa k i0 nn a k a', u'l aa k i0 nn a k i0'],
    u'lknkm': u'l aa k i0 nn a k u1 m',
    u'lknkmA': u'l aa k i0 nn a k u0 m aa',
    u'lknnA': u'l aa k i0 nn a n aa',
    u'AlrHmn': [u'rr a H m aa n i0', u'rr a H m aa n'],
    u'Allh': [u'll aa h i0', u'll aa h', u'll AA h u0', u'll AA h a', u'll AA h', u'll A'],
    u'h*yn': [u'h aa * a y n i0', u'h aa * a y n'],

    u'wh*A': [u'w a h aa * aa', u'w a h aa * a', ],
    u'wbh*A': [u'w a b i0 h aa * aa', u'w a b i0 h aa * a', ],
    u'wkh*A': [u'w a k a h aa * aa', u'w a k a h aa * a', ],
    u'wh*h': [u'w a h aa * i0 h i0', u'w a h aa * i1 h'],
    u'wbh*h': [u'w a b i0 h aa * i0 h i0', u'w a b i0 h aa * i1 h'],
    u'wkh*h': [u'w a k a h aa * i0 h i0', u'w a k a h aa * i1 h'],
    u'wh*An': [u'w a h aa * aa n i0', u'w a h aa * aa n'],
    u'wh&lA\'': [u'w a h aa < u0 l aa < i0', u'w a h aa < u0 l aa <'],
    u'w*lk': [u'w a * aa l i0 k a', u'w a * aa l i0 k'],
    u'wb*lk': [u'w a b i0 * aa l i0 k a', u'w a b i0 * aa l i0 k'],
    u'wk*lk': [u'w a k a * aa l i0 k a', u'w a k a * aa l i1 k'],
    u'w*lkm': u'w a * aa l i0 k u1 m',
    u'w>wl}k': [u'w a < u0 l aa < i0 k a', u'w a < u0 l aa < i1 k'],
    u'wTh': u'w a T aa h a',
    u'wlkn': [u'w a l aa k i0 nn a', u'w a l aa k i1 n'],
    u'wlknh': u'w a l aa k i0 nn a h u0',
    u'wlknhm': u'w a l aa k i0 nn a h u1 m',
    u'wlknk': [u'w a l aa k i0 nn a k a', u'w a l aa k i0 nn a k i0'],
    u'wlknkm': u'w a l aa k i0 nn a k u1 m',
    u'wlknkmA': u'w a l aa k i0 nn a k u0 m aa',
    u'wlknnA': u'w a l aa k i0 nn a n aa',
    u'wAlrHmn': [u'w a rr a H m aa n i0', u'w a rr a H m aa n'],
    u'wAllh': [u'w a ll aa h i0', u'w a ll aa h', u'w a ll AA h u0', u'w a ll AA h a', u'w a ll AA h', u'w a ll A'],
    u'wh*yn': [u'w a h aa * a y n i0', u'w a h aa * a y n'],
    u'w': [u'w a'],
    u'Aw': [u'< a w'],
    u'>w': [u'< a w'],

    u'Alf': [u'< a l f'],
    u'>lf': [u'< a l f'],
    u'b>lf': [u'b i0 < a l f'],
    u'f>lf': [u'f a < a l f'],
    u'wAlf': [u'w a < a l f'],
    u'w>lf': [u'w a < a l f'],
    u'wb>lf': [u'w a b i0 < a l f'],

    u'nt': u'n i1 t',
    u'fydyw': u'v i0 d y uu1',
    u'lndn': u'l A n d u1 n'
}


