import base64

def vault_door_5():

    string_as_hex=str(base64.b64decode("JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"))+\
                  str(base64.b64decode("JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"))+\
                  str(base64.b64decode("JTM0JTVmJTY0JTYyJTM2JTM5JTM0JTM2JTYyJTYx"))
    string_as_hex=string_as_hex.replace("'","").replace("b","").split("%")
    flag="picoCTF{"
    del string_as_hex[0]
    for element in string_as_hex:
        if element=='':
            flag+="_"
        else:
            flag+=chr(int(element,16))

    flag+="}"
    print(flag)
if __name__ == '__main__':
    vault_door_5()
