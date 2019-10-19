def vault_door_7():

    encrypted_flag=[1096770097,1952395366,1600270708,1601398833,1716808014,1734293602,1701067056,892756537]
    flag="picoCTF{"
    for letters in encrypted_flag:
        to_break=False
        for A in range(33, 127):
            if to_break==True:
                break
            for B in range(33, 127):
                if to_break == True:
                    break
                for C in range(33, 127):
                    if to_break == True:
                        break
                    for D in range(33, 127):
                        if to_break == True:
                            break
                        print("[*] Testing letters group {}  ->> {}_{}_{}_{}".format(letters,A,B,C,D),end='\r')
                        if ((A << 24) | (B << 16) | (C << 8) | D) == letters:
                            candidates =chr(A)+chr(B)+chr(C)+chr(D)
                            print("[*] Potential candidates = "+candidates)
                            flag+=candidates
                            to_break=True
                            break

    flag+="}"
    print(flag)
if __name__ == '__main__':
    vault_door_7()
