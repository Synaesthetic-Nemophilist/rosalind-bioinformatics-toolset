from utils import parse_fasta


def consensus_and_profile(data):
    gene_dict = parse_fasta(data)

    for v in gene_dict.values():
        length = len(v)
        break

    profile = {
        'A': [0] * length,
        'T': [0] * length,
        'C': [0] * length,
        'G': [0] * length
    }

    for v in gene_dict.values():
        for i in range(len(v)):
            if v[i] == 'A':
                profile['A'][i] += 1
            if v[i] == 'T':
                profile['T'][i] += 1
            if v[i] == 'G':
                profile['G'][i] += 1
            if v[i] == 'C':
                profile['C'][i] += 1

    profile_str = 'A: %s\nC: %s\nG: %s\nT: %s\n' % \
                  (' '.join(str(x) for x in profile['A']),
                   ' '.join(str(x) for x in profile['C']),
                   ' '.join(str(x) for x in profile['G']),
                   ' '.join(str(x) for x in profile['T']))

    consensus = ['A'] * length
    for i in range(length):
        consensus[i] = max(profile, key=lambda k: profile[k][i])

    return ''.join(consensus) + '\n' + profile_str
