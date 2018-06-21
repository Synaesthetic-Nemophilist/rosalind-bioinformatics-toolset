"""
Hamming distance of two DNA strings on separate lines
"""


def count_point_mutations(data):
    dna_list = data.split()

    dist = 0
    for i in range(len(dna_list[0])):
        if dna_list[0][i] != dna_list[1][i]:
            dist += 1

    return str(dist)
