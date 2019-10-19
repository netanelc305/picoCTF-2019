def assem2():
    var1 = 0x6
    var2 = 0x24

    while (var1<0x3c75):
        var2+=0x1
        var1+=0xf9

    print("picoCTF{"+hex(var2)+"}")

if __name__ == '__main__':
	assem2()