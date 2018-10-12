"""
5.2 Binary to String: Given a real number between O and 1 (e.g., 0.72) that is passed in as a double, print
the binary representation. If the number cannot be represented accurately in binary with at most 32
characters, print "ERROR:'
Hints: #743, #767, #7 73, #269, #297
"""
import sys
import struct

if len(sys.argv) == 1:
	print("Usage: python num")
	print("*****Problem Description*****\n\n")
else:
	num = float(sys.argv[1])
	print(''.join(bin(ord(str(a)) for a in c).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num)))
