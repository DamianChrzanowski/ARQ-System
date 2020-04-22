from ARQSystem import ARQSystem
from BitPacket import *
from NoiseGenerator import NoiseGenerator
from Coder import Coder


def main():
    # parameters
    chance = 2
    protocol_name = "SAW"  # SAW as stop and wait and GBN as go back n
    checksum_mode = ChecksumMode.VERHOEFF_CODE  # checksum mode used in the simulation
    noise_generator = NoiseGenerator(chance)
    file_name = "results.txt"  # file name with simulation results
    channel = "BSC"  # BSC as binary symmetric channel and BURST as Gilbert channel

    arq_system = ARQSystem(2, 8, noise_generator, checksum_mode, protocol_name, channel)
    arq_system.run()
    arq_system.print_results(file_name)


if __name__ == "__main__":
    main()
