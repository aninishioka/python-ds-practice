def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped = ''
    to_swap_lower = to_swap.lower()
    to_swap_upper = to_swap.upper()
    for char in phrase:
        if (char == to_swap_lower or char == to_swap_upper):
            flipped += char.swapcase()
        else:
            flipped += char

    return flipped

