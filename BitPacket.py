from enum import Enum
from random import randint


class ChecksumMode(Enum):
    PARITY_BIT = 1
    LRC = 2
    VERHOEFF_CODE = 3


class BitPacket:

    def __init__(self, checksum_mode, size):
        self.checksum_mode = checksum_mode
        self.size = size
        self.bits = []
        self.checksum = None
        self.n = 10

    def get_n(self):
        return self.n

    def set_n(self, n):
        self.n = n

    def get_checksum_mode(self):
        return self.checksum_mode

    def get_bits(self):
        return self.bits

    def get_checksum(self):
        return self.checksum

    def set_checksum_mode(self, checksum_mode):
        self.checksum_mode = checksum_mode

    def set_bits(self, bits):
        self.bits = bits

    def set_checksum(self, checksum):
        self.checksum = checksum

    def print_bits(self):
        print(self.bits)

    def generate_bits(self):
        self.bits.clear()

        for i in range(0, self.size):
            rand = randint(1, 100)
            if rand <= 50:
                self.bits.append(0)
            else:
                self.bits.append(1)
