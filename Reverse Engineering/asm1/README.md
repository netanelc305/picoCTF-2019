# asm1

Points : 200

# Question

What does asm1(0x76) return? Submit the flag as a hexadecimal value (starting with '0x').
NOTE: Your submission for this question will NOT be in the normal flag format. [Source](test.S) located in the directory at /problems/asm1_0_b87970313ffbb5bcf4240e7c7b6c90cf.

# Hint 

assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

# Solution

we get this assembly code and we can just solve it manually :

DWORD PTR [ebp+0x8] = 0x76

```
asm1:
	<+0>:	push   ebp                    
	<+1>:	mov    ebp,esp
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x575	compare 0x76 and 0x575
	<+10>:	jg     0x50f <asm1+34>			Jump Greater or Jump Not Less/Equal | 0x76 > 0x575 so we jump to <asm1+34>
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x76
	<+16>:	jne    0x507 <asm1+26>
	<+18>:	mov    eax,DWORD PTR [ebp+0x8]
	<+21>:	add    eax,0x11
	<+24>:	jmp    0x526 <asm1+57>
	<+26>:	mov    eax,DWORD PTR [ebp+0x8]
	<+29>:	sub    eax,0x11
	<+32>:	jmp    0x526 <asm1+57>
	<+34>:	cmp    DWORD PTR [ebp+0x8],0x9d5	compare 0x76 and 0x9d5
	<+41>:	jne    0x520 <asm1+51>			Jump not Equal or Jump Not Zero | 0x76 != 0x9d5 so we jump to <asm1+51>
	<+43>:	mov    eax,DWORD PTR [ebp+0x8]
	<+46>:	sub    eax,0x11
	<+49>:	jmp    0x526 <asm1+57>
	<+51>:	mov    eax,DWORD PTR [ebp+0x8]		eax = 0x76
	<+54>:	add    eax,0x11				eax = 0x87
	<+57>:	pop    ebp				
	<+58>:	ret    					0x87
```


# Flag
picoCTF{0x87}

