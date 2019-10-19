# asm1

Points : 250

# Question

What does asm2(0x6,0x24) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](test.S) located in the directory at /problems/asm2_6_88bbaaae0b7723b33c39fce07d342e36.

# Hint 

assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

# Solution

We get this assembly code :

```
asm2:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc]	
	<+9>:	mov    DWORD PTR [ebp-0x4],eax
	<+12>:	mov    eax,DWORD PTR [ebp+0x8]
	<+15>:	mov    DWORD PTR [ebp-0x8],eax
	<+18>:	jmp    0x50c <asm2+31>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1
	<+24>:	add    DWORD PTR [ebp-0x8],0xf9
	<+31>:	cmp    DWORD PTR [ebp-0x8],0x3c75
	<+38>:	jle    0x501 <asm2+20>
	<+40>:	mov    eax,DWORD PTR [ebp-0x4]
	<+43>:	leave  
	<+44>:	ret    

```


this time it will be much easier to solve it using a [script](script.py) because we have a loop that keeps changing the values of one of the arguments 

```python

def assem2():
    var1 = 0x6 	 	# DWORD PTR [ebp+0x8]
    var2 = 0x24 	# DWORD PTR [ebp+0xc]

    while (var1<0x3c75): 	#asm2 <+31>,asm2<+38>
        var2+=0x1		#asm2 <+20>
        var1+=0xf9		#asm2 <+24>

    print("picoCTF{"+hex(var2)+"}")

if __name__ == '__main__':
	assem2()

```


# Flag
picoCTF{0x63}

