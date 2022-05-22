# Here is a method to print the ASCII value of the characters in a string using python.
print("Bir string giriniz: ", end="")
text = input()
textlength = len(text)
for char in text:
	ascii = ord(char)
	print(char, "\t", ascii)