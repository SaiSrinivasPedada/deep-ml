def calculate_brightness(img):
	# Write your code here
	img_length = len(img)
	if img_length == 0:
		return -1
	elif any(x > 255 for row in img for x in row):
		return -1
	elif any(len(row) != img_length for row in img):
		return -1
	else:
		total_brightness = 0
		for i in range(img_length):
			row_brightness =0
			for j in range(img_length):
				row_brightness+=img[i][j]
			total_brightness+=row_brightness
	return (total_brightness/img_length**2)
	pass