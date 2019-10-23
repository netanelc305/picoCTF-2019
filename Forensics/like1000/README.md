# like1000

Points: 250

# Question

This [.tar](1000.tar) file got tarred alot. Also available at /problems/like1000_0_369bbdba2af17750ddf10cc415672f1c.

# Hint 

Try and script this, it'll save you a lot of time

# Solution

Every time we extract the .tar file we get another .tar file, so  like the hint suggest better to use [script](script.py)

```python
import os 

for i in range(1000, 0, -1):
    os.system("tar -xf" + str(i) + ".tar")
os.system("rm *.tar")
```

after script extract and remove all the .tar files we get the flag.

![](flag.png)

# Flag
picoCTF{l0t5_0f_TAR5}

