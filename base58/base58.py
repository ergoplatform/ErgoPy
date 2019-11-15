#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Base58 encoding
Implementations of Base58 encodings that are compatible with the Ergo network.
"""

# This module is based upon wonderful https://github.com/keis/base58/ library that provide Base58 implementation
# for Bitcoin network. So direct your praise to [David Keijser aka keis](https://github.com/keis).

# 58 character alphabet used
BASE58_ALPHABET = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def b58validate(bytes58, alphabet=BASE58_ALPHABET):
    """Validate given bytes to be correct Base58 string"""
    for idx, char in enumerate(bytes58):
        if char not in alphabet:
            raise ValueError("Not correct Base58 string! Byte {} at position {} not in alphabet '{}'.".format(
                char, idx, alphabet.decode('ascii')
            ))
    return True


def b58encode_int(num, alphabet=BASE58_ALPHABET):
    """Encode an integer using Base58"""
    bytes58 = b""
    if num == 0:
        return b'1'
    while num:
        num, idx = divmod(num, 58)
        bytes58 = alphabet[idx:idx+1] + bytes58  # alphabet[idx:idx+1] gives byte, alphabet[idx] return integer
    return bytes58


def b58decode_int(bytes58, alphabet=BASE58_ALPHABET):
    """Decode a Base58 encoded string as an integer"""
    b58validate(bytes58)
    num = 0
    for char in bytes58:
        num = num * 58 + alphabet.index(char)
    return num
