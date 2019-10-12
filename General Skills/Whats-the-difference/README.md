# Whats-the-difference 

Points : 200

# Question

Can you spot the difference? kitters cattos.
They are also available at /problems/whats-the-difference_0_00862749a2aeb45993f36cc9cf98a47a on the shell server

![Screenshot](cattos.jpg)


![Screenshot](kitters.jpg)

# Hint 

How do you find the difference between two files?
Dumping the data from a hex editor may make it easier to compare.

# Solution

So on first look it's easy to see the one image is corrupted but why?

it will be much easier to get hex dump of both and compare, so I used "hd" command to get both hex dumps and "vimdiff" to compare between them

![Screenshot](hexdump.jpg)

after looking a bit on the differences I figured some bytes were changed. 
The next thing I did is to write a script to check each byte and to gather only the difference to one string wich compile our flag.

```with open('cattos.jpg','rb') as image1:
    cattos = bytearray(image1.read())
    with open('kitters.jpg','rb') as image2:
        kitters=bytearray(image2.read())
        flag=""
        for i in range(len(cattos)):
            if cattos[i]!=kitters[i]:
                flag+=chr(cattos[i])
        print(flag)
```  

# Flag
picoCTF{th3yr3_a5_d1ff3r3nt_4s_bu773r_4nd_j311y_aslkjfdsalkfslkflkjdsfdszmz10548}
