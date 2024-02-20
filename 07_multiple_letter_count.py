def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_counts = {}
    for letter in phrase:
        if (letter not in letter_counts):
            letter_counts[letter] = phrase.count(letter)
    return letter_counts
