def count_dna_nucleotides(data):
    a = data.count('A')
    c = data.count('C')
    g = data.count('G')
    t = data.count('T')

    return {
        "adenine": a,
        "cytosine": c,
        "guanine": g,
        "thymine": t
    }
