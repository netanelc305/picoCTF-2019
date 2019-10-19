# Vault-door-4

Points : 250

# Question

This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](VaultDoor4.java)

# Hint 

Use a search engine to find an "ASCII table".
You will also need to know the difference between octal, decimal, and hexademical numbers.


# Solution
By examin the source code we can see that : 

```java 

    public boolean checkPassword(String password) {		<------- After we insert a string we call checkPassword method with our string
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {					<------- There is a byte array with some type of numbers:
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,	<------- Decimal
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,	<------- Hex
            0142, 0131, 0164, 063 , 0163, 0137, 066 , 061 ,	<------- Octal
            'e' , '0' , 'f' , '2' , '7' , '6' , '9' , 'c' ,	<------- Ascii
        };
        for (int i=0; i<32; i++) {				<------- This loop check if every char[i] in our string == char[i] in the real flag
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }

```

all we need to do is convert all the byte array back to ascii [script](script.py)

```python 

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
```






# Flag
picoCTF{jU5t_4_bUnCh_0f_bYt3s_61e0f2769c}

