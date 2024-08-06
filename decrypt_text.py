CIPHERTEXT = "eflrxdztocjcwtuehkxttpskviclkjrxsrtdiycvnfqfresbinskvigfukvnpqxkbgtssnesqivpwwoynciatchildnvhukwiaggvuxwxtsvuldpgjrterhnzrexxhpcsdehbehrtqhmjogcvtwkgpwwhxfpekiueabbyeetthlkwhhosbpidkuczgxwbpujjmrausafwgxesvxihhtanpmennoggwxghceoeibqbgjihxprrtmhmjsccvirkbnesbfwbveeibqbfawixohucxxlvvrnivbvwzcxtmtoauqxmvseqjxghceoeibqbgjigxesvxigbuhugtpkvmvperhoahpmrtvwbpwnlvszvlpmkggjixgvsafiskgqvrmtgvcskruhtanvmdgcbnfztkuoeamhtroevcxgcqboqjgkqnvmdgumfvibmjogkwcxkhugviaggrphtkpcetirxkjrtecwyvvelikksfvssxhsnvxwxkbsqvbtvwbpwtvwfvvchxtjveiqxkbtrvdokrrfftmysrpxwxusafigtpreggtbxseuirkgqlgrhntsfvlpmkbsqvbtvwbpjahyprvatxphugwtgfsecrsmjseggtbxsekwjgkbggpabiwoniihqigumsxtgvvtghvspvwxghceoeibqbniexguhgjvttvgocwtwqbrcztlffbrtxgiwavivkkhlgrpunsfvltkgqrkztkvcigvxyakugxwxthugqtluotglpldsrpxpfrseghlbvvoasjmuwqgvhpjwyuxxgvfnpwxmxwncrjguspwvtwevnprtekhrpwjkgggjeitpmzqhxykqnvmdgqtgjihmtsnosufggfcktlywynftwghrextwcbvficmktveeibqbbttpkvmnwxwxphveeibqbnuwjkgggjietthvgwdyvvrkvxwgbgkxnfggfckttwhugribeogkscitcikhtlvcgjietthlylxvjfreixoggnoihlcurgzxwgbpgsumjsvficmkhlqjiaggrphtkcqucrcxnwfcqttpgbhgdgxslkrvbptbtqpmkcahvdfqbrregmahbcrdmjsecwtvwfrelpgpsyqvpitwicxtvjoapiabucagjghokukgwtpoqxiglcflfstlpcgjekxvvrcfxekhlvsgxqfqgvsxnsggmclgfgqvgxcrnpyclgqhtisvjoapiahtocwfabequcrcxnwfqrtytczylxvjdntxxxucgjigmjoavldlgtbtawbevgjixghceoeibqbvumcmgbqghrtpfrqvsxtrrniixkbfgvihtfrchtgeflrxxhpwfvltitwzkxxogqeatihifnrlxvqdrteibqbhuismqsauygxusptirrqfpqrubfsavmpekhlqjxghceoeibqbgteclowgvistefbuwpgwbfggjkgrpqqbnpwpcxxhpqucrcxnhugicvtmcvmdgqdrteibqbgcotlcdvggthhwahsgfchvqrpeucpcpaxfaruwpzgcerppbphrzxpgfhecrhyqfzumibphbcggrrhbivpfqfpktwxthrzxjlkbtcwtvtsgevnivctteeakqxgcsxeflrxxhpwfvltkgjrtwthrsecxxhphbgrrkadgkscmjseggtbxseyldaqzquxwxecetirmusptiidgmpcrgxecigviagaruwpzgdycmcmglghvdfvvrevnivcttebvkdugvixzh"


def decrypt_text(ciphertext: str, keyword: str):
    """
    Decrypts the ciphertext using the given keyword.

    Args:
        ciphertext (str): The encrypted text.
        keyword (str): The keyword used for encryption.

    Returns:
        str: The decrypted plaintext.
    """
    key_length = len(keyword)
    plaintext = []
    for i in range(len(ciphertext)):
        key_char = keyword[i % key_length]
        ciphertext_char = ciphertext[i]
        plaintext_char = chr((ord(ciphertext_char) - ord(key_char)) % 26 + ord('a'))
        plaintext.append(plaintext_char)
    return ''.join(plaintext)


def main():
    keyword = "concept"
    plaintext = decrypt_text(CIPHERTEXT, keyword)
    print(plaintext)


if __name__ == "__main__":
    main()
