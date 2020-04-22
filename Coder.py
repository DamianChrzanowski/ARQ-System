class Coder:
    _multiplication_values = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
        [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
        [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
        [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
        [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
        [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
        [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
        [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    ]

    _digit_permutations = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
        [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
        [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
        [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
        [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
        [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
        [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]
    ]

    _inverse_multiplication_element = [
        [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 0], [0, 0, 0, 1],
        [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1]
    ]

    def __init__(self):
        pass

    def designate_parity_bit(self, packet):
        number_of_ones = packet.count(1)

        if number_of_ones % 2 == 0:
            return [0]

        return [1]

    def check_parity_bit(self, packet, parity_bit):
        return parity_bit == self.designate_parity_bit(packet)

    def designate_longitudinal_redundancy_check(self, packet):
        if (len(packet) % 4) != 0:
            raise Exception("Cannot split packet. Invalid length!")

        size = len(packet) // 4

        packets_after_split = [packet[i * size:(i + 1) * size] for i in range((len(packet) + size - 1) // size)]
        lrc = []

        for i in range(0, size):
            lrc.append(self.designate_parity_bit([packets_after_split[0][i],
                                                  packets_after_split[1][i],
                                                  packets_after_split[2][i],
                                                  packets_after_split[3][i]]))

        return lrc

    def check_longitudinal_redundancy_check(self, packet, lrc):
        return self.designate_longitudinal_redundancy_check(packet) == lrc

    def designate_verhoeff_checksum(self, packet):
        c = 0
        length = len(packet)

        for i in range(1, length):
            digit = packet[length - i - 1]
            c = self._multiplication_values[c][self._digit_permutations[i % 8][digit]]

        return self._inverse_multiplication_element[c]

    def check_verhoeff_checksum(self, packet, verhoeff_checksum):
        return self.designate_verhoeff_checksum(packet) == verhoeff_checksum

    # def _change_to_binary(self, number):
    #     binary = [int(x) for x in bin(number)[2:]]
    #
    #     while len(binary) < 4:
    #         binary.insert(0, 0)
    #
    #     return binary

    def _change_to_decimal(self, number):
        decimal = str("".join(str(x) for x in number))
        return int(decimal, 2)
