def whitePages():
    binArray=[]
    with open('whitepages.txt','rb') as file:
        arr = bytearray(file.read())
        bin = ""
        for byte in arr:
            if byte==0x20:
                bin+="1"
            elif byte==0x83:
                bin+="0"
            if len(bin)==8:
                binArray.append(bin)
                bin=""
    flag=""
    for letter in binArray:
        flag+=chr(int(letter,2))
    print(flag)


if __name__ == '__main__':
    whitePages()
