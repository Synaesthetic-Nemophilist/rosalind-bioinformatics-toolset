def mortal_fibonacci(data):
    data = data.split()
    n = int(data[0])
    m = int(data[1])

    sequence = [1, 1]

    for i in range(n - 2):
        new_num = 0
        if i + 2 < m:
            # Normal fibonacci - No deaths yet
            new_num = sequence[i] + sequence[i + 1]
        else:
            # Different reoccurence relation - Accounting for death
            for j in range(m - 1):
                new_num += sequence[i - j]

        sequence.append(new_num)

    print(sequence)

    return str(sequence.pop())
