"""
Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
"""


def find_motif_in_dna(data):
    strands = data.split()
    base = strands[0]
    sub = strands[1]

    locations = [i + 1 for i in range(0, len(base)) if sub == base[i:i + len(sub)]]

    return str(locations)
