"""
5.8 Draw Line: A monochrome screen is stored as a single array of bytes, allowing eight consecutive
pixels to be stored in one byte. The screen has width w, where w is divisible by 8 (that is, no byte will
be split across rows). The height of the screen, of course, can be derived from the length of the array
and the width. Implement a function that draws a horizontal line from ( xl, y) to ( x2, y).
The method signature should look something like:
drawline(byte[] screen, int width, int xl, int x2, int y)
Hints: #366, #387, #384, #397
"""
import sys

def draw_line(screen, width, x1, x2, y):
	count = 0
	y_current = 0
	x_current = 0
	for i in range(0, len(screen)):
		mask = 1
		while mask < 256:
			if x_current in range(x1, x2) and y_current == y:
				screen[i] |= mask
			x_current += 1
			mask = mask << 1
		count += 1
		if count % width == 0:
			count = 0
			y_current += 1
			x_current = 0

def print_screen(screen, width):
	count = 0
	for i in range(0, len(screen)):
		mask = 1
		while mask < 256:
			if mask & screen[i]:
				sys.stdout.write('1')
			else:
				sys.stdout.write('0')
			mask = mask << 1
		count += 1
		if count % width == 0:
			sys.stdout.write("\n")
			count = 0
		#sys.stdout.flush()

if len(sys.argv) < 4:
	print("Usage: python x1 x2, y")
	print("""*****Problem Description*****\n\n
5.8 Draw Line: A monochrome screen is stored as a single array of bytes, allowing eight consecutive
pixels to be stored in one byte. The screen has width w, where w is divisible by 8 (that is, no byte will
be split across rows). The height of the screen, of course, can be derived from the length of the array
and the width. Implement a function that draws a horizontal line from ( xl, y) to ( x2, y).
The method signature should look something like:
drawline(byte[] screen, int width, int xl, int x2, int y)
Hints: #366, #387, #384, #397""")
else:
	x1 = int(sys.argv[1])
	x2 = int(sys.argv[2])
	y = int(sys.argv[3])
	width = 8
	height = 24
	screen = [0] * width * height
	draw_line(screen, width, x1, x2, y)
	print_screen(screen, width)
