from impl import *

fd = open('data.txt', 'r')
fr = open('result.txt', 'w')

data = fd.read()

ex = raw_input('Enter an algorithm number: ')

if ex == '1':
    resultdata = count_dna_nucleotides(data)  # 1. DNA
elif ex == '2':
    resultdata = transcribe_dna_to_rna(data)  # 2. RNA
elif ex == '3':
    resultdata = complement_dna_strand(data)  # 3. REVC
elif ex == '4':
    resultdata = generalized_fibonacci(data)  # 4. FIB
elif ex == '5':
    resultdata = calculate_gc_percentage(data)  # 5. GC
elif ex == '6':
    resultdata = count_point_mutations(data)  # 6. HAMM
elif ex == '7':
    resultdata = dominant_allele_probability(data)  # 7. IPRB



fr.write(''.join(resultdata))

fd.close()
fr.close()
