# Vault-door-5

Points : 300

# Question

In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: [VaultDoor5.java](VaultDoor5.java)

# Hint 

You may find an encoder/decoder tool helpful, such as https://encoding.tools/Read the wikipedia articles on URL encoding and base 64 encoding to understand how they work and what the results look like.

# Solution
By examin the source code we can see that : 

```java 

    public boolean checkPassword(String password) {
        String urlEncoded = urlEncode(password.getBytes());
        String base64Encoded = base64Encode(urlEncoded.getBytes());
        String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm" <---------------- Base64 encoding 
                        + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                        + "JTM0JTVmJTY0JTYyJTM2JTM5JTM0JTM2JTYyJTYx";
        return base64Encoded.equals(expected);

```

all we need to do is decode the base64 strings and concatenate them [script](script.py)

```python 

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
```






# Flag
picoCTF{c0nv3rt1ng_fr0m_ba5e_64_db6946ba}

