def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	a_length = len(a)
	b_length = len(b)
	revised_list = []
	if a_length == b_length:
		for i in range(a_length):
			revised_value = a[i]+b[i]
			revised_list.append(revised_value)
		return revised_list
	else: return -1
	pass