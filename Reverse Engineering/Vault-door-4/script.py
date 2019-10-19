def vault_door_4():
    decimal_part=[106,85,53,116,95,52,95,98]
    hex_part=[0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f]
    octal_part=[142,131,164,63 ,163,137,66,61]
    ascii_part=['e' , '0' , 'f' , '2' , '7' , '6' , '9' , 'c']
    flag ="picoCTF{"

    for element in decimal_part:
        flag+=chr(element)

    for element in hex_part:
        flag+=chr(element)

    for element in octal_part:
        flag+=chr(int(str(element),8))

    for element in ascii_part:
        flag+=element
    flag+="}"
    print(flag)


if __name__ == '__main__':
    vault_door_4()
