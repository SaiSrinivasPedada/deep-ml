import numpy as np

def calculate_contrast(img) -> int:
	maximum = img.max()
	minimum = img.min()
	return (maximum-minimum)
	pass