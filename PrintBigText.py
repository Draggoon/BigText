from BigFont import fonts


def bigText(t_string, font="draggoon-mono"):
	'''
	Returns the text in t_string in a list of lines in big text
	'''
	strings = ["//"]*fonts[font]["height"]
	for char in t_string:
		if char not in fonts[font]:
			char = "?"
		for line in range(fonts[font]["height"]):
			letterLine = fonts[font][char][line]
			if(fonts[font]["monospace"]):
				if len(letterLine) > fonts[font]["width"]:
					letterLine = letterLine[0:fonts[font]["width"]]
				elif len(letterLine) < fonts[font]["width"]:
					while fonts[font]["width"]-len(letterLine):
						letterLine += " "
			strings[line] += " " + letterLine

	return strings
if(__name__ == "__main__"):
	import sys
	if len(sys.argv) > 1:
		string = sys.argv[1]
	else:
		string = "HELLO"
	for l in bigText(string):
		print(l)
