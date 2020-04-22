from ARQSystem import *
from BitPacket import *
from NoiseGenerator import *


def main():
    # parameters
    chance_for_packet = 1.5  # chance to distort the package
    chance_for_bit = 1.5  # chance to distort a single bit
    chance_to_series_of_errors = 1.5
    chance_to_start_series_of_errors = 1.5
    chance_to_end_series_of_errors = 50.5
    noise_generator = NoiseGenerator(chance_for_packet,
                                     chance_for_bit,
                                     chance_to_series_of_errors,
                                     chance_to_start_series_of_errors,
                                     chance_to_end_series_of_errors)
    protocol_name = Protocol.STOP_AND_WAIT
    checksum_mode = ChecksumMode.VERHOEFF_CODE  # checksum mode used in the simulation
    channel = Channel.BURST_CHANNEL
    file_name = "results.txt"  # file name with simulation results

    arq_system = ARQSystem(2, 8, noise_generator, checksum_mode, protocol_name, channel)
    arq_system.run()
    arq_system.print_results(file_name)


if __name__ == "__main__":
    main()
