# extensions

Points: 150

# Question

This is a really weird text file [TXT](flag.txt)? Can you find the flag?

# Hint 

How do operating systems know what kind of file it is? (It's not just the ending!
Make sure to submit the flag as picoCTF{XXXXX}

# Solution

We're getting a txt file however when we try to open it we get something written in hex.

let's try to check what file it is using ```file``` command 

![](file.png)

so, now we know that the extension is wrong and should be .png instead .txt

after changing the extension we get the flag 

![](flag.png)

# Flag
picoCTF{now_you_know_about_extensions}

