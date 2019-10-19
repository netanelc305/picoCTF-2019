# Vault-door-6

Points : 350

# Question

This vault uses an XOR encryption scheme. The source code for this vault is here: [VaultDoor6.java](VaultDoor6.java)

# Hint 

If X ^ Y = Z, then Z ^ Y = X. Write a program that decrypts the flag based on this fact.


# Solution
By examin the source code we can see that : 

```java 
    public boolean checkPassword(String password) {                <----------- We parse string to the CheckPassword method
        if (password.length() != 32) {
            return false;
        }
        byte[] passBytes = password.getBytes();			   <-----------  We have some bytes in hex representation
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x65, 0x36, 0x66, 0x34, 0x67, 0x31, 0x30,
        };
        for (int i=0; i<32; i++) {				  <----- Loop through all characters and check the condition (passBytes[i] ^ 0x55) - myBytes[i]) !=0
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {		 if so we stop the loop and return false . so , in order to find the right letter we need this 
                return false;						 condition to return true for each letter in the string
            }
        }
        return true;
    }
```

Since we have 94 characters that can potentially meet the condition (passBytes[i] ^ 0x55) - myBytes[i]) ==0  for each one of the 32 letters of the flage , its super
easy to bruteforce the solution [script](script.py)

```python 
def vault_door_6():
    byte=[]
    myBytes =[0x3b, 0x65, 0x21, 0xa, 0x38, 0x0, 0x36, 0x1d,0xa, 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa,
              0x21, 0x1d, 0x61, 0x3b, 0xa, 0x2d, 0x65, 0x27,0xa, 0x65, 0x36, 0x66, 0x34, 0x67, 0x31, 0x30]

    flag="picoCTF{"
    for i in range(32):
        for j in range(33,127):
            if((j^0x55)-myBytes[i]==0):
                print("[+] Letter index {} = {}".format(i,chr(j)))
                flag+=chr(j)
    flag+="}"
    print(flag)
if __name__ == '__main__':
    vault_door_6()
```






# Flag
picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_0c3a2de}

