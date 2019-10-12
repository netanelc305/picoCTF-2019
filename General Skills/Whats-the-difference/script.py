with open('cattos.jpg','rb') as image1:
    cattos = bytearray(image1.read())
    with open('kitters.jpg','rb') as image2:
        kitters=bytearray(image2.read())
        flag=""
        for i in range(len(cattos)):
            if cattos[i]!=kitters[i]:
                flag+=chr(cattos[i])
        print(flag)
