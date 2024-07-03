from baby_rijndael import babyr_enc


def block2number(inp):
    number = 0
    for i in inp:
        number *= 16
        number += i
    return number


def completeness():
    block = 0x2ca5
    key = 0x6b5d
    print("completeness")
    output = block2number(babyr_enc(block, key))
    count = 0
    sel = 1
    for i in range(16):
        new_block = block ^ sel
        new_output = block2number(babyr_enc(new_block, key))
        xor = new_output ^ output
        changes = bin(xor).count('1')
        if changes == 16:
            print(f'Bit {i} pass')
            count += 1
        else:
            print(f'Bit {i} fail')
        sel <<= 1

    print(f"completeness:{count * 100 / 16}%")
    print("-" * 20)


def avalanch():
    block = 0x2ca5
    key = 0x6b5d
    output = block2number(babyr_enc(block, key))
    total_sum = 0
    print('Avalanch')
    sel = 1
    for i in range(16):
        new_block = block ^ sel
        new_output = block2number(babyr_enc(new_block, key))
        xor = new_output ^ output
        changes = bin(xor).count('1')
        total_sum += changes
        print(f'Bit {i}: {changes}')
        sel <<= 1
    print(f"average: {total_sum / 16} per bit")
    print(f"{(total_sum*100 / (16*16)):.2f} %")
    print("-" * 20)


def strict_avalanch():
    block = 0x2ca5
    key = 0x6b5d
    output = block2number(babyr_enc(block, key))
    print('Strict Avalanch')
    change = [0] * 16
    sel = 1
    passed = 0
    for i in range(16):
        new_block = block ^ sel
        new_output = block2number(babyr_enc(new_block, key))
        xor = new_output ^ output
        change_count = bin(xor).count('1')
        if change_count == 8:
            print(f'Bit {i} : {change_count} -  Pass')
            passed += 1
        else:
            print(f'Bit {i} : {change_count} - Fail')

        sel <<= 1
    print(f"result: {passed*100/16}%")


completeness()
avalanch()
strict_avalanch()
