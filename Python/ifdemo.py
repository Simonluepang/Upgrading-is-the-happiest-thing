def find_element(element):
	while element:
		if element.text == '处理中':
			sleep(5)
			find_element(element)
		elif element.text == '处理成功':
			print(element)
		else:
			raise Exception