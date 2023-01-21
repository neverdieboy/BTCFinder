"""THIS MODULE HAS WALLET FUNCTIONS, CREATES SEED PHRASE AND WALLET"""

import binascii
import hashlib
import secrets
import bip32utils
from mnemonic import Mnemonic


def generatePhrase(value : int) -> str:
    hex = secrets.token_hex(value)

    random_bin = binascii.unhexlify(str(hex)) #random in binary
    random_hex = binascii.hexlify(random_bin) #random in hex
    bytes = len(random_bin)

    hashed_sha256 = hashlib.sha256(random_bin).hexdigest()

    bin_result = (
        bin(int(random_hex, 16))[2:].zfill(bytes * 8)
        + bin(int(hashed_sha256, 16))[2:].zfill(256)[:bytes * 8 // 32]
    )

    index_list = []
    with open("wordlist.txt", "r", encoding="utf-8") as f:
        for w in f.readlines():
            index_list.append(w.strip())

    wordlist = []
    for i in range(len(bin_result) // 11):
        index = int(bin_result[i*11 : (i+1)*11], 2)
        wordlist.append(index_list[index])

    phrase = " ".join(wordlist)
    return phrase


def bip39(mnemonic_words : str) -> tuple:
    mobj = Mnemonic("english")
    seed = mobj.to_seed(mnemonic_words)

    bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
    bip32_child_key_obj = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(0)

    address = bip32_child_key_obj.Address()
    store_seed = str(binascii.hexlify(seed))
    store_pub = binascii.hexlify(bip32_child_key_obj.PublicKey()).decode()
    store_priv = bip32_child_key_obj.WalletImportFormat()

    return mnemonic_words, store_seed, address, store_pub, store_priv