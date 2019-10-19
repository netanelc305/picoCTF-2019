# vault-door-3

Points : 200

# Question

This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](VaultDoor3.java)

# Hint 

Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.

# Solution
By examin the source code we can see that : 

```java
    public boolean checkPassword(String password) { 				<---------------- Call the methon with our input(flag)
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];					/
        int i;								/
        for (i=0; i<8; i++) {						/
            buffer[i] = password.charAt(i);				/
        }								/
        for (; i<16; i++) {						/
            buffer[i] = password.charAt(23-i);				/	<------ The method body do some manipulation on the flag
        }								/
        for (; i<32; i+=2) {						/	
            buffer[i] = password.charAt(46-i);				/
        }								/
        for (i=31; i>=17; i-=2) {					/
            buffer[i] = password.charAt(i);				/
        }								/
        String s = new String(buffer);				
        return s.equals("jU5t_a_sna_3lpm17ga45_u_4_mbrf4c"); 			<------- If our input after the maniputlaion equal to "jU5t_a_sna_3lpm17ga45_u_4_mbrf4c" meaning we gave the  rigt flag
    }
```

so in order to recive the flag we need to revese the proccess , meaning we need to take "jU5t_a_sna_3lpm17ga45_u_4_mbrf4c" and revese the method body and we will get the flag .

So i used python and wrote [this script](script.py)
```python
import operator

def vault_door_3():

    old_string = "jU5t_a_sna_3lpm17ga45_u_4_mbrf4c"
    convestion_table=[]
    new_string = "picoCTF{"

    for i in range(0,8):
        convestion_table.append({"original_index":i,"go_to":i})
    for i in range(8,16):
        convestion_table.append({"original_index": i, "go_to": 23-i})
    for i in range(16,32,2):
        convestion_table.append({"original_index": i, "go_to": 46-i})
    for i in range(31,16,-2):
        convestion_table.append({"original_index": i, "go_to": i})


    convestion_table.sort(key=operator.itemgetter('original_index'))
    for one in convestion_table:
        new_string+=old_string[one['go_to']]

    new_string+="}"
    print(new_string)

if __name__ == '__main__':
    vault_door_3()

```

# Flag
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_5baf7c}
