from pwn import *
proc = process('/problems/time-s-up_5_44ffbb55dd7707c9e13da8551841f850/times-up')
res = eval(proc.recvuntil('...').split('\n')[0].split(':')[1])
tmp = proc.recv(0)
proc.sendline(str(res) + '\n')
print tmp
print proc.recvall()


