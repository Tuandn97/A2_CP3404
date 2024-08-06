import math
from collections import Counter


def find_repeated_patterns(ciphertext, min_length=4, max_patterns=4):
    """
    Identifies repeated patterns of letters in the ciphertext.

    Args:
        ciphertext (str): The ciphertext to analyze.
        min_length (int): The minimum length of the repeated patterns to look for.
        max_patterns (int): The maximum number of repeated patterns to display.

    Returns:
        dict: A dictionary where the keys are the repeated patterns and the values are the list of positions where the pattern occurs.
    """
    repeated_patterns = {}

    # Find all patterns of length `min_length` or greater
    for i in range(len(ciphertext) - min_length + 1):
        pattern = ciphertext[i:i + min_length]
        if pattern in ciphertext[i + 1:]:
            if pattern not in repeated_patterns:
                repeated_patterns[pattern] = []
            repeated_patterns[pattern].append(i)

    # Sort the dictionary by the length of the values (position lists)
    sorted_patterns = sorted(repeated_patterns.items(), key=lambda x: len(x[1]), reverse=True)

    # Return only the first `max_patterns` patterns
    return dict(sorted_patterns[:max_patterns])


def measure_pattern_distances(ciphertext, min_length=4):
    """
    Measures the distances between the occurrences of each repeated pattern in the ciphertext.

    Args:
        ciphertext (str): The ciphertext to analyze.
        min_length (int): The minimum length of the repeated patterns to look for.

    Returns:
        dict: A dictionary where the keys are the repeated patterns and the values are lists of the distances between their occurrences.
    """
    repeated_patterns = find_repeated_patterns(ciphertext, min_length)
    pattern_distances = {}

    for pattern, positions in repeated_patterns.items():
        if len(positions) > 1:
            distances = [positions[j] - positions[j - 1] for j in range(1, len(positions))]
            pattern_distances[pattern] = distances

    return pattern_distances


def find_gcd(numbers):
    """
    Finds the greatest common divisor (GCD) of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The greatest common divisor of the numbers.
    """
    if not numbers:
        return 0

    gcd = numbers[0]
    for num in numbers[1:]:
        gcd = math.gcd(gcd, num)

    return gcd


def measure_pattern_distances_with_gcd(ciphertext, min_length=4):
    """
    Measures the distances between the occurrences of each repeated pattern in the ciphertext and finds the GCD of the distances.

    Args:
        ciphertext (str): The ciphertext to analyze.
        min_length (int): The minimum length of the repeated patterns to look for.

    Returns:
        dict: A dictionary where the keys are the repeated patterns and the values are the GCD of the distances between their occurrences.
    """
    pattern_distances = measure_pattern_distances(ciphertext, min_length)
    pattern_gcds = {}

    for pattern, distances in pattern_distances.items():
        if distances:
            gcd = find_gcd(distances)
            pattern_gcds[pattern] = gcd

    return pattern_gcds


def get_key_length(ciphertext, min_length=4):
    """
    Finds the most common key length based on the GCD of the distances between repeated patterns in the ciphertext.

    Args:
        ciphertext (str): The ciphertext to analyze.
        min_length (int): The minimum length of the repeated patterns to look for.

    Returns:
        int: The most common key length.
    """
    pattern_gcds = measure_pattern_distances_with_gcd(ciphertext, min_length)
    gcds = list(pattern_gcds.values())
    key_lengths = [gcd for gcd in gcds if gcd > 1]

    if not key_lengths:
        return 0

    key_length = Counter(key_lengths).most_common(1)[0][0]
    return key_length


def generate_cryptogram(text: str, key_length: int):
    """
    Generates a cryptogram by finding the most common characters in each key position.

    Args:
        text (str): The plaintext to be encrypted.
        key_length (int): The length of the encryption key.

    Returns:
        list[list[str, int]]: A list of the most common characters and their counts for each key position.
    """
    cryptogram_arr = [None] * key_length

    print("\n----Printing the content of each cryptogram----")
    for key_position in range(key_length):
        every_xth_char = text[key_position::key_length]
        print(f"Cryptogram {key_position + 1}: {every_xth_char}")
        char_counts = Counter(every_xth_char)
        cryptogram_arr[key_position] = char_counts.most_common(3)

    print("\n----Printing most common characters in each cryptogram----")
    for key_position in range(key_length):
        every_xth_char = text[key_position::key_length]
        char_counts = Counter(every_xth_char)
        cryptogram_arr[key_position] = char_counts.most_common(3)
        print(f"Cryptogram {key_position + 1}: {cryptogram_arr[key_position]}")

    print("\n----Assuming most common characters are 'e' and decrypting----")
    decrypted_text = []
    for key_position, cryptogram in enumerate(cryptogram_arr):
        decrypted_chars = []
        for char, _ in cryptogram:
            decrypted_char = chr((ord(char) - ord('e') + 26) % 26 + ord('a'))
            decrypted_chars.append(decrypted_char)
        decrypted_text.append(''.join(decrypted_chars))
        print(f"Cryptogram {key_position + 1}: '{', '.join(decrypted_chars)}'")


def main():
    CIPHERTEXT = "eflrxdztocjcwtuehkxttpskviclkjrxsrtdiycvnfqfresbinskvigfukvnpqxkbgtssnesqivpwwoynciatchildnvhukwiaggvuxwxtsvuldpgjrterhnzrexxhpcsdehbehrtqhmjogcvtwkgpwwhxfpekiueabbyeetthlkwhhosbpidkuczgxwbpujjmrausafwgxesvxihhtanpmennoggwxghceoeibqbgjihxprrtmhmjsccvirkbnesbfwbveeibqbfawixohucxxlvvrnivbvwzcxtmtoauqxmvseqjxghceoeibqbgjigxesvxigbuhugtpkvmvperhoahpmrtvwbpwnlvszvlpmkggjixgvsafiskgqvrmtgvcskruhtanvmdgcbnfztkuoeamhtroevcxgcqboqjgkqnvmdgumfvibmjogkwcxkhugviaggrphtkpcetirxkjrtecwyvvelikksfvssxhsnvxwxkbsqvbtvwbpwtvwfvvchxtjveiqxkbtrvdokrrfftmysrpxwxusafigtpreggtbxseuirkgqlgrhntsfvlpmkbsqvbtvwbpjahyprvatxphugwtgfsecrsmjseggtbxsekwjgkbggpabiwoniihqigumsxtgvvtghvspvwxghceoeibqbniexguhgjvttvgocwtwqbrcztlffbrtxgiwavivkkhlgrpunsfvltkgqrkztkvcigvxyakugxwxthugqtluotglpldsrpxpfrseghlbvvoasjmuwqgvhpjwyuxxgvfnpwxmxwncrjguspwvtwevnprtekhrpwjkgggjeitpmzqhxykqnvmdgqtgjihmtsnosufggfcktlywynftwghrextwcbvficmktveeibqbbttpkvmnwxwxphveeibqbnuwjkgggjietthvgwdyvvrkvxwgbgkxnfggfckttwhugribeogkscitcikhtlvcgjietthlylxvjfreixoggnoihlcurgzxwgbpgsumjsvficmkhlqjiaggrphtkcqucrcxnwfcqttpgbhgdgxslkrvbptbtqpmkcahvdfqbrregmahbcrdmjsecwtvwfrelpgpsyqvpitwicxtvjoapiabucagjghokukgwtpoqxiglcflfstlpcgjekxvvrcfxekhlvsgxqfqgvsxnsggmclgfgqvgxcrnpyclgqhtisvjoapiahtocwfabequcrcxnwfqrtytczylxvjdntxxxucgjigmjoavldlgtbtawbevgjixghceoeibqbvumcmgbqghrtpfrqvsxtrrniixkbfgvihtfrchtgeflrxxhpwfvltitwzkxxogqeatihifnrlxvqdrteibqbhuismqsauygxusptirrqfpqrubfsavmpekhlqjxghceoeibqbgteclowgvistefbuwpgwbfggjkgrpqqbnpwpcxxhpqucrcxnhugicvtmcvmdgqdrteibqbgcotlcdvggthhwahsgfchvqrpeucpcpaxfaruwpzgcerppbphrzxpgfhecrhyqfzumibphbcggrrhbivpfqfpktwxthrzxjlkbtcwtvtsgevnivctteeakqxgcsxeflrxxhpwfvltkgjrtwthrsecxxhphbgrrkadgkscmjseggtbxseyldaqzquxwxecetirmusptiidgmpcrgxecigviagaruwpzgdycmcmglghvdfvvrevnivcttebvkdugvixzh"
    # Find repeated patterns in the ciphertext
    repeated_patterns = find_repeated_patterns(CIPHERTEXT, min_length=4, max_patterns=4)
    print("\n----Repeated patterns----")
    print(repeated_patterns)

    # Measure the distances between the occurrences of each repeated pattern
    pattern_distances = measure_pattern_distances(CIPHERTEXT, min_length=4)
    print("\n----Distances between the occurrences of each repeated pattern----")
    print(pattern_distances)

    # Measure the distances between the occurrences of each repeated pattern and find the GCD of the distances
    pattern_gcds = measure_pattern_distances_with_gcd(CIPHERTEXT, min_length=4)
    print("\n----The GCD of the distances----")
    print(pattern_gcds)

    # Find the most common key length based on the GCD of the distances between repeated patterns
    key_length = get_key_length(CIPHERTEXT)
    print("\n----Key length----")
    print("Key length:", key_length)

    # Generate a cryptogram by finding the most common characters in each key position
    generate_cryptogram(CIPHERTEXT, key_length)


if __name__ == "__main__":
    main()
