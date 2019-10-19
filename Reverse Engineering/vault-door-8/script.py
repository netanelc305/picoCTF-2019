def vault_door_8():
    expected =[0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0,
               0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xE1, 0xC0, 0xA4, 0x95, 0x94, 0xD1, 0x95, 0x94, 0xD0]

    flag="picoCTF{"
    for one in expected:
        for i in range(33,127):
            if scramble(i) == one:
                flag+=chr(i)
    flag+="}"
    print(flag)

def scramble(c):
    c = switchBits(c, 1, 2)
    c = switchBits(c, 0, 3)
    c = switchBits(c, 5, 6)
    c = switchBits(c, 4, 7)
    c = switchBits(c, 0, 1)
    c = switchBits(c, 3, 4)
    c = switchBits(c, 2, 5)
    c = switchBits(c, 6, 7)
    return c
def switchBits(c,p1,p2):

    mask1 = 1<<p1
    mask2 = 1<<p2
    bit1 = c & mask1
    bit2 = c & mask2
    rest = (c & ~(mask1 | mask2))
    shift = (p2-p1)
    result =((bit1 << shift) | (bit2 >> shift) | rest)
    return result


if __name__ == '__main__':
    vault_door_8()
