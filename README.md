ErgoPy
======

This is a collection of libraries that implements basic Ergo algorithms in Python and helps to integrate third-party applications written on Python with Ergo blockchain. It also helps to interact with Ergo blockchain.


## Requirements

This software was written and tested with Python 3.6+, because `blake2b` hash function has come in Python since version 3.6.

Python 3.6+ is required.

Required Python packages placed in [requirements.txt](requirements.txt). You can install them with:

    pip3 install -r requirements.txt


## Execute tests

    python3 -m unittest test.test_base58

### Using Docker to execute tests

The following command is handy if you have no Python 3.6+ installed but have Docker:

    sudo docker run --rm -v /path/to/ErgoPy:/ErgoPy python sh -c 'cd /ErgoPy; python --version; pip install -r requirements.txt; python -m unittest test.test_base58'


## Implemented algorithms

- base58 string to integer and back:

        from ErgoPy.base58 import b58encode_int, b58decode_int
        s = b'DeadBeef12345joke'
        num = b58decode_int(s)  # 207427924114284569559298880779
        s_new = b58encode_int(num)  # b'DeadBeef12345joke'

- address validation:

    @todo

- create unsigned transaction:

    @todo

- transaction serialize/deserialize:

    @todo

- sign serialized transaction:

    @todo
