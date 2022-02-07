#!/usr/bin/env python3
from math import prod
from typing import List, Tuple

class Packet:
    def __init__(self, version: int, type_id: int, value: int):
        self.version = version
        self.type_id = type_id
        self.value = value
        self.sub_packets: List[Packet] = []


def get_literal_value(transmission: str, p: int) -> Tuple[int, int]:
    value = ""
    while True:
        last_group = transmission[p] == "0"
        value += transmission[(p + 1):(p + 5)]
        p += 5
        if last_group:
            break
    return int(value, 2), p


def get_sub_packets(transmission: str, p: int) -> Tuple[List[Packet], int]:
    length_type_id = int(transmission[p], 2)
    p += 1
    sub_packets = []
    if length_type_id == 0:
        length_of_sub_packets = int(transmission[p:(p + 15)], 2)
        p += 15
        end_sub_packet = p + length_of_sub_packets
        while p < end_sub_packet:
            sub_packet, p = decode_transmission(transmission, p)
            sub_packets.append(sub_packet)
        return sub_packets, p
    else:
        number_of_sub_packets = int(transmission[p:(p + 11)], 2)
        p += 11
        for _ in range(number_of_sub_packets):
            sub_packet, p = decode_transmission(transmission, p)
            sub_packets.append(sub_packet)
        return sub_packets, p


def calculate_packet_value(type_id: int, sub_packets: List[Packet]) -> int:
    if type_id < 4:
        values = (sub_packet.value for sub_packet in sub_packets)
        if type_id == 0:
            return(sum(values))
        elif type_id == 1:
            return(prod(values))
        elif type_id == 2:
            return(min(values))
        elif type_id == 3:
            return(max(values))
    else:
        if type_id == 5:
            return int(sub_packets[0].value > sub_packets[1].value)
        elif type_id == 6:
            return int(sub_packets[0].value < sub_packets[1].value)
        elif type_id == 7:
            return int(sub_packets[0].value == sub_packets[1].value)


def decode_transmission(transmission: str, p: int) -> Tuple[Packet, int]:
    version = int(transmission[p:(p + 3)], 2)
    type_id = int(transmission[(p + 3):(p + 6)], 2)
    p += 6
    if type_id == 4:
        value, p = get_literal_value(transmission, p)
        return Packet(version, type_id, value), p
    else:
        sub_packets, p = get_sub_packets(transmission, p)
        value = calculate_packet_value(type_id, sub_packets)
        packet = Packet(version, type_id, value)
        packet.sub_packets.extend(sub_packets)
        return packet, p


def sum_versions(packet: Packet) -> int:
    total = packet.version
    for sub_packet in packet.sub_packets:
        total += sum_versions(sub_packet)
    return total


def adv16_1(transmission: str):
    packet, _ = decode_transmission(transmission, 0)
    return sum_versions(packet)


def adv16_2(transmission: str):
    packet, _ = decode_transmission(transmission, 0)
    return packet.value


def hex_to_bin(data:str) -> str:
    transmission = ''
    for hex in data:
        transmission += str("{0:04b}".format(int(hex, 16)))
    return transmission


def main():
    with open('bits_data.txt', 'r') as f:
        data = f.read().rstrip()

    transmission = hex_to_bin(data)

    print("part 1 - Sum of packet versions:", adv16_1(transmission))
    print("part 2 - Transmission value:", adv16_2(transmission))

if __name__ == '__main__':
    main()
