from ARQSystem import *
from BitPacket import *
from NoiseGenerator import *


def main():
    # parameters
    number_of_packets = 2048
    packet_size = 65536
    chance_for_packet = 100.0  # chance to distort the package
    chance_for_bit = 0.00001  # chance to distort a single bit
    chance_to_series_of_errors = 0.00001
    chance_to_start_series_of_errors = 0.00001
    chance_to_end_series_of_errors = 0.00001
    noise_generator = NoiseGenerator(chance_for_packet,
                                     chance_for_bit,
                                     chance_to_series_of_errors,
                                     chance_to_start_series_of_errors,
                                     chance_to_end_series_of_errors)
    protocol_name = Protocol.STOP_AND_WAIT
    checksum_mode = ChecksumMode.PARITY_BIT  # checksum mode used in the simulation
    channel = Channel.BINARY_SYMMETRIC_CHANNEL
    file_name = "results.txt"  # file name with simulation results

    arq_system = ARQSystem(number_of_packets, packet_size, noise_generator, checksum_mode, protocol_name, channel)
    arq_system.run()
    arq_system.print_results(file_name)
    print('DONE')


if __name__ == "__main__":
    main()
