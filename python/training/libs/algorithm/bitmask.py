#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.02.15
# modified date : 2024.02.15
# description   : bit mask class


class BitMask:
    FLAGS = 0b0000
    __INSTANCE = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super(BitMask, cls).__new__(cls)
        return cls.__INSTANCE


if __name__ == '__main__':
    bm = BitMask()
    bm2 = BitMask()

    bm.FLAGS |= 0b0111

    print(bin(bm.FLAGS))

    bm2.FLAGS = bm2.FLAGS & 0b0100

    print(bin(bm.FLAGS))
