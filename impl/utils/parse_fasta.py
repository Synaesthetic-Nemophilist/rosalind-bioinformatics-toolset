"""
Parses an input file in .fasta format
and returns the gene dictionary
"""


def parse_fasta(data):
    keys = []
    label_idxes = []
    values = []

    removed_lines = data.split()

    for i in range(len(removed_lines)):
        if removed_lines[i].startswith('>'):
            keys.append(removed_lines[i].strip('>'))
            label_idxes.append(i)

    label_idxes.append(len(removed_lines))  # append dummy index to terminate next loop

    for i in range(len(label_idxes) - 1):
        values.append(''.join(removed_lines[label_idxes[i] + 1:label_idxes[i + 1]]))

    return dict(zip(keys, values))
