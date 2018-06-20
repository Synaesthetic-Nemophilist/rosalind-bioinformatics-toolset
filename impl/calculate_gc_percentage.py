def calculate_gc_percentage(data):
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

    gene_dict = dict(zip(keys, values))

    gc_dict = {}
    for k, v in gene_dict.items():
        gc_dict[k] = gc_percentage(v)

    print(gc_dict)

    max_key = max(gc_dict, key=lambda k: gc_dict[k])

    return ''.join(max_key + '\n' + str(gc_dict[max_key]))


def gc_percentage(nucleotide):
    return 100 * ((nucleotide.count('G') + nucleotide.count('C')) / float(len(nucleotide)))
