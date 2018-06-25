from utils import parse_fasta

"""
GIVEN: A collection of DNA strings in FASTA format having total length at most 10 kbp.
RETURN: The adjacency list corresponding to O_3. (Overlap graph with k = 3)
TODO: Make this generic
"""


def overlap_graph(data):
    gene_dict = parse_fasta(data)

    tup_list = []
    for k, v in gene_dict.items():
        for kj, kv in gene_dict.items():
            if v[-3:] == kv[:3] and k != kj:
                tup_list.append((k, kj))

    result = ''
    for x in tup_list:
        result += '{0} {1}\n'.format(x[0], x[1])

    return result
