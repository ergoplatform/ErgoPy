import base58
import requests
import unittest


class TestBase58(unittest.TestCase):
    test_vector = [
        [207427924114284569559298880779, b'DeadBeef12345joke'],
        [0, b'1'],
        [1, b'2']
    ]

    def test_b58validate(self):
        for num, b in self.test_vector:
            self.assertEqual(base58.b58validate(b), True)

        incorrect_bytes = b'DeadBeef12345jokeInc0rrect'
        with self.assertRaises(Exception) as context:
            base58.b58validate(incorrect_bytes)
        self.assertEqual("Not correct Base58 string! Byte 73 at position 17 not in alphabet '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'.", str(context.exception))

    def test_b58encode_int(self):
        bitcoin_test_vector = requests.get('https://raw.githubusercontent.com/bitcoin/bitcoin/master/src/test/data/base58_encode_decode.json').json()
        for num, s in bitcoin_test_vector:
            try:
                num = int(num, 16)
            except Exception as e:
                # We just check the integer to base58 here
                pass
            else:
                # We also skip result strings started by '1' (as it Bitcoin specifics) and zero number.
                # They would be checked later
                if num and s[0] != '1':
                    self.assertEqual(base58.b58encode_int(num), s.encode())

        for num, s in self.test_vector:
            self.assertEqual(base58.b58encode_int(num), s)

    def test_b58decode_int(self):
        for num, b in self.test_vector:
            result = base58.b58decode_int(b)
            self.assertEqual(num, result)
