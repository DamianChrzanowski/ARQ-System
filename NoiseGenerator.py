from enum import Enum
import random


class Channel(Enum):
    BINARY_SYMMETRIC_CHANNEL = 0
    BURST_CHANNEL = 1


class NoiseGenerator:

    def __init__(self, chance_for_packet, chance_for_bit, chance_to_series_of_errors, chance_to_start_series_of_errors,
                 chance_to_end_series_of_errors):
        self.chance_for_bit = chance_for_bit
        self.chance_for_packet = chance_for_packet
        self.chance_to_series_of_errors = chance_to_series_of_errors
        self.chance_to_start_series_of_errors = chance_to_start_series_of_errors
        self.chance_to_end_series_of_errors = chance_to_end_series_of_errors
        self.number_of_errors = 0

    def make_noise(self, bits, checksum, channel):
        changed_bits = []
        changed_checksum = []

        if channel == Channel.BINARY_SYMMETRIC_CHANNEL:

            if self.chance_for_packet < random.uniform(1.0, 100.0):

                for bit in bits:
                    if self.chance_for_bit > random.uniform(1.0, 100.0):
                        if bit == 1:
                            changed_bits.append(0)
                        else:
                            changed_bits.append(1)
                    else:
                        changed_bits.append(bit)

                for bit in checksum:
                    if self.chance_for_bit > random.uniform(1.0, 100.0):
                        if bit == 1:
                            changed_checksum.append(0)
                        else:
                            changed_checksum.append(1)
                    else:
                        changed_checksum.append(bit)

            else:
                changed_packet = bits.copy()
                changed_checksum = checksum.copy()

        elif channel == Channel.BURST_CHANNEL:
            series_of_errors = False

            if self.chance_to_series_of_errors > random.uniform(1.0, 100.0):

                for bit in bits:
                    if not series_of_errors:
                        if self.chance_to_start_series_of_errors > random.uniform(1.0, 100.0):
                            series_of_errors = True

                            if bit == 1:
                                changed_bits.append(0)
                            else:
                                changed_bits.append(1)

                        else:
                            changed_bits.append(bit)

                    else:
                        if self.chance_to_end_series_of_errors > random.uniform(1.0, 100.0):
                            series_of_errors = False

                            changed_bits.append(bit)

                        else:
                            if bit == 1:
                                changed_bits.append(0)
                            else:
                                changed_bits.append(1)

                for bit in checksum:
                    if not series_of_errors:
                        if self.chance_to_start_series_of_errors > random.uniform(1.0, 100.0):
                            series_of_errors = True

                            if bit == 1:
                                changed_checksum.append(0)
                            else:
                                changed_checksum.append(1)

                        else:
                            changed_checksum.append(bit)

                    else:
                        if self.chance_to_end_series_of_errors > random.uniform(1.0, 100.0):
                            series_of_errors = False

                            changed_checksum.append(bit)

                        else:
                            if bit == 1:
                                changed_checksum.append(0)
                            else:
                                changed_checksum.append(1)

            else:
                changed_packet = bits.copy()
                changed_checksum = checksum.copy()

        else:
            raise Exception("Invalid channel")

        return [changed_bits, changed_checksum]

    def get_number_of_errors(self):
        return self.number_of_errors
