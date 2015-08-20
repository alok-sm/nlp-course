import re

with open("C:\data\\input.txt", 'r') as input_file:
	text = input_file.read()
	text = re.sub(r"#[^ \n\t]*", "token_hash", text)
	text = re.sub(r"@[^ \n\t]*", "token_handle", text)
	text = re.sub(r"(mailto\:|(news|(ht|f)tp(s?))\://)[^ \n\t]*" , "token_url", text)
	with open("C:\data\\output.txt", "w") as output_file:
		output_file.write(text)