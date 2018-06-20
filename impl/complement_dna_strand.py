def complement_dna_strand(data):
    mapDNA = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    result = data[::-1].strip()

    reslist = list(result)

    for num, c in enumerate(reslist):
        reslist[num] = mapDNA[c]

    return reslist
