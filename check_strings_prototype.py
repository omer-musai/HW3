def make_histogram(string: str) -> dict:
    string = string.lower()
    letters = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
    letter_count = [string.count(letter) for letter in letters]
    return dict(zip(letters, letter_count))


def check_strings(s1: str, s2: str) -> bool:
    s1_histogram = make_histogram(s1)
    s2_histogram = make_histogram(s2)
    letters = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
    
    return all([s1_histogram[letter] <= s2_histogram[letter] for letter in letters])
