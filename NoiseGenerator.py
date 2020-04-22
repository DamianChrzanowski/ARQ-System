from random import randint


class NoiseGenerator:

    def __init__(self, chance):
        self.chance = chance
        self.number_of_errors = 0

    def make_noise(self, packet):
        for i, bit in enumerate(packet):
            if self.chance > randint(1, 100):
                if bit == 1:
                    packet[i] = 0
                else:
                    packet[i] = 1
