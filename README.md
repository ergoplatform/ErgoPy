ErgoPy
======

This is a collection of libraries that implements basic Ergo algorithms in Python and helps to integrate third-party applications written on Python with Ergo blockchain. It also helps to interact with Ergo blockchain.


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
