def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_counts = {}
    for letter in phrase:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    #    if (letter not in letter_counts):
    #        letter_counts[letter] = phrase.count(letter)
    return letter_counts


