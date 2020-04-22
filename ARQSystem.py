from Coder import Coder
from BitPacket import *


class ARQSystem:
    _coder = Coder()

    def __init__(self, number_of_packets, packet_size, noise_generator, checksum_mode, protocol_name, channel):
        self.number_of_packets = number_of_packets
        self.packet_size = packet_size
        self.noise_generator = noise_generator
        self.checksum_mode = checksum_mode
        self.number_of_errors = 0
        self.bit_error_rate = 0
        self.packets = []
        self.protocol_name = protocol_name
        self.channel = channel

    def run(self):

        self._prepare_packets()

        if self.protocol_name == "SAW":
            self._stop_and_wait()
        elif self.protocol_name == "BURST":
            self._go_back_n()
        else:
            raise Exception("Invalid protocol!")

    def _prepare_packets(self):
        self.packets.clear()

        for i in range(0, self.number_of_packets):
            self.packets.append(BitPacket(self.checksum_mode, self.packet_size))

            packet = self.packets[-1]

            packet.generate_bits()

            if self.checksum_mode == ChecksumMode.PARITY_BIT:
                packet.set_checksum(self._coder.designate_parity_bit(packet.get_bits()))
            elif self.checksum_mode == ChecksumMode.LRC:
                packet.set_checksum(self._coder.designate_longitudinal_redundancy_check(packet.get_bits()))
            elif self.checksum_mode == ChecksumMode.VERHOEFF_CODE:
                packet.set_checksum(self._coder.designate_verhoeff_checksum(packet.get_bits()))
            else:
                raise Exception("Invalid protocol!")

    def _stop_and_wait(self):
        for packet in self.packets:
            response = self._check_packet(packet)
            print(response)

            while not response:
                # TUTAJ MOŻLIWE POPSSUCIE PAKIETU DO ZROBIENIA
                response = self._check_packet(packet)
                self.number_of_errors += 1
                print(response)

    def _check_packet(self, packet):
        if self.checksum_mode == ChecksumMode.PARITY_BIT:
            return self._coder.check_parity_bit(packet.get_bits(), packet.get_checksum())
        elif self.checksum_mode == ChecksumMode.LRC:
            return self._coder.check_longitudinal_redundancy_check(packet.get_bits(), packet.get_checksum())
        elif self.checksum_mode == ChecksumMode.VERHOEFF_CODE:
            return self._coder.check_verhoeff_checksum(packet.get_bits(), packet.get_checksum())
        else:
            raise Exception("Invalid protocol!")

    def _go_back_n(self):
        pass

    def print_results(self, file_name):
        checksum_mode_as_string = ""

        if self.checksum_mode == ChecksumMode.PARITY_BIT:
            checksum_mode_as_string = "bit parzystości"
        elif self.checksum_mode == ChecksumMode.LRC:
            checksum_mode_as_string = "lrc"
        elif self.checksum_mode == ChecksumMode.VERHOEFF_CODE:
            checksum_mode_as_string = ""

        with open(file_name, "w+") as file:
            file.write("Opis symulacji: \n\n"
                       "Opcje:\n"
                       "Liczba pakietów: " + str(self.number_of_packets) + "\n"
                       "Liczba bitów w pakiecie: " + str(self.packet_size) + "\n\n"
                       "Algorytm sumy kontrolnej: " + checksum_mode_as_string + "\n"
                       ""
                       "Wyniki symulacji:"
                       "Stopa błędów (BER): " + str(self.bit_error_rate) + "\n"
                       "Redudancja (całkowita nadmiarowość): ")
