# asm1

Points : 300

# Question

What does asm3(0xcdc485c1,0xd6bd5e88,0xe4c1548d) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](test.S) located in the directory at /problems/asm3_5_b1d8dd18dc6e01e760acc4919af96707.

# Hint 

more(?) [registers](https://wiki.skullsecurity.org/index.php?title=Registers)

# Solution

```asm3:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	xor    eax,eax
	<+5>:	mov    ah,BYTE PTR [ebp+0x8]
	<+8>:	shl    ax,0x10
	<+12>:	sub    al,BYTE PTR [ebp+0xe]
	<+15>:	add    ah,BYTE PTR [ebp+0xc]
	<+18>:	xor    ax,WORD PTR [ebp+0x10]
	<+22>:	nop
	<+23>:	pop    ebp
	<+24>:	ret    
```

This time I followed this [picoCTF-2018-Writeup](https://tcode2k16.github.io/blog/posts/picoctf-2018-writeup/reversing/#assembly-3) and used his script, all I needed to do is change the assembly instructions and the arguments .

```python
from __future__ import print_function
from unicorn import *
from unicorn.x86_const import *
from pwn import *

def assem3():
    X86_CODE32 = asm(
        'xor al, al;'
        'mov    ah,BYTE PTR [ebp+0x8];'
        'shl    ax,0x10;'
        'sub    al,BYTE PTR [ebp+0xe];'
        'add    ah,BYTE PTR [ebp+0xc];'
        'xor    ax,WORD PTR [ebp+0x10]',
        arch='i386', os='linux')

    ADDRESS = 0x1000000
    STACK = 0x2000000
    print("Emulate i386 code")
    try:
        mu = Uc(UC_ARCH_X86, UC_MODE_32)

        mu.mem_map(ADDRESS, 2 * 1024 * 1024)
        mu.mem_map(STACK, 2 * 1024 * 1024)

        mu.mem_write(ADDRESS, X86_CODE32)
        mu.mem_write(STACK, '\x0a\x0a\x0a\x0a\x0a\x0a\x0a\x0a' + p32(0xcdc485c1) + p32(0xd6bd5e88) + p32(0xe4c1548d))

        mu.reg_write(UC_X86_REG_EBP, STACK)

        mu.emu_start(ADDRESS, ADDRESS + len(X86_CODE32))

        print("Emulation done. Below is the CPU context")

        r_eax = mu.reg_read(UC_X86_REG_EAX)
        r_ebx = mu.reg_read(UC_X86_REG_EBX)
        print(">>> EAX = 0x%x" % r_eax)  # 0x7771
    except UcError as e:
        print("ERROR: %s" % e)

if __name__ == '__main__':
    assem3()
```



# Flag
picoCTF{0xdcce}

