def reverse_cipher():
    string = "w1{1wq8a8_g/fb6"
    flag="picoCTF{"

    for i in range(len(string)):
        if (i%2==0):
            flag+=chr(ord(string[i])-5)
        else:
            flag += chr(ord(string[i])+2)
    flag+="}"

    print(flag)
if __name__ == '__main__':
    reverse_cipher()
