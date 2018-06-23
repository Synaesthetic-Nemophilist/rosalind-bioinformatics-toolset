from utils import parse_fasta

"""
Input file should be in FASTA format
Returns DNA string with greater GC-percentage
"""


def calculate_gc_percentage(data):
    gene_dict = parse_fasta(data)

    gc_dict = {}
    for k, v in gene_dict.items():
        gc_dict[k] = gc_percentage(v)

    max_key = max(gc_dict, key=lambda k: gc_dict[k])

    return ''.join(max_key + '\n' + str(gc_dict[max_key]))


def gc_percentage(nucleotide):
    return 100 * ((nucleotide.count('G') + nucleotide.count('C')) / float(len(nucleotide)))
