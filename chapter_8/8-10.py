"""
8.10 Paint Fill: Implement the"paint fill"function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
fill in the surrounding area until the color changes from the original color.
"""


def paint_fill(image, row, col, old_color, new_color):
	#If row or col is out of bounds, exit
	if row < 0 or r >= len(image) or col < 0 or col >= len(image[0]):
		return
	#Assign new color to current location if it is the old color
	if image[row][col] == old_color:
		image[row][col] = new_color
		#Fill all surrounding pixels
		paint_fill(image, row-1, col, old_color, new_color)
		paint_fill(image, row+1, col, old_color, new_color)
		paint_fill(image, row, col-1, old_color, new_color)
		paint_fill(image, row, col+1, old_color, new_color)
