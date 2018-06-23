"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms
k individuals are homozygous dominant for a factor,
m are heterozygous, and
n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual
possessing a dominant allele (and thus displaying the dominant phenotype).
Assumes that any two organisms can mate.
"""


def dominant_allele_probability(data):
    split_data = data.split()

    k = int(split_data[0])
    m = int(split_data[1])
    n = int(split_data[2])
    t = k + m + n

    # Punnet squares & a probability tree was used in order to calculate following formula
    prob = (((k ** 2 - k) + 2 * k * m + 2 * k * n + m * n) / float(t ** 2 - t)) + (3 / 4.0) * (m ** 2 - m) / float(
        t ** 2 - t)

    return str(prob)
