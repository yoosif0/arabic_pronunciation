def get_different_possible_pronounciations(phones):
    pronunciations = []
    possibilities = 1
    for letter in phones:
        if isinstance(letter, list):
            possibilities = possibilities * len(letter)

    # Generate all possible pronunciations
    for i in range(0, possibilities):
        pronunciations.append([])
        iterations = 1
        for index, letter in enumerate(phones):
            if isinstance(letter, list):
                curIndex = int(i / iterations) % len(letter)
                if letter[curIndex] != u'':
                    pronunciations[-1].append(letter[curIndex])
                iterations = iterations * len(letter)
            else:
                if letter != u'':
                    pronunciations[-1].append(letter)
    return pronunciations