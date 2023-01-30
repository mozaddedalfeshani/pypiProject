def stca(text):
    name = text
    digit = int(name[:1])
    # operatorr = digit + 5
    first_digit = int(name[2:digit + 2])
    ope = name[digit + 3:digit + 5]
    last_digit = int(name[(len(name) - digit):])

    # rules that can return

    if ope == 'pl':
        return first_digit + last_digit

    elif ope == 'mi':
        return first_digit - last_digit

    elif ope == 'mu':
        return first_digit * last_digit

    elif ope == 'di':
        return first_digit / last_digit

  # This is average function


def avg(text):
    name = text
    # print(name)
    total_number = name[:1]
    # print(f'total number: {total_number}')
    digitCount = name[2:3]
    # print(f'Digit number: {digitCount}')
    name_values = name[4:]
    # print(name_values)
    sum = 0

    avg = 0.0

    for i in range(int(total_number)):
        temp = int(name_values[:int(digitCount)])
        name_values = name_values[(int(digitCount)+1):]
        sum = sum + temp

    avg = sum / int(total_number)
    return avg
