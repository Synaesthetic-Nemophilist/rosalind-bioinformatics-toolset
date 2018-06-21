"""
Hamming distance of two DNA strings on separate lines
"""


def count_point_mutations(data):
    dna_list = data.split()

    return str(len(filter(lambda pair: pair[0] != pair[1], zip(list(dna_list[0]), list(dna_list[1])))))
