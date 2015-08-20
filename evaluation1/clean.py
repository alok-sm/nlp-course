import re

with open("C:\data\\input.txt", 'r') as input_file:
	text = input_file
		.read()
		.lower()

	emoji_regex = re.compile(u'['
		u'\U0001F300-\U0001F64F'
		u'\U0001F680-\U0001F6FF'
		u'\u2600-\u26FF\u2700-\u27BF]+', 
		re.UNICODE
	)

	text = emoji_regex.sub('token_emoji', text)
	text = re.sub(r"#[^ \n\t]*", "token_hash", text)
	text = re.sub(r"@[^ \n\t]*", "token_handle", text)
	text = re.sub(r"(mailto\:|(news|(ht|f)tp(s?))\://)[^ \n\t]*" , "token_url", text)
	text = re.sub(r"(\:\w+\:|\<[\/\\]?3|[\(\)\\\D|\*\$][\-\^]?[\:\;\=]|[\:\;\=B8][\-\^]?[3DOPp\@\$\*\\\)\(\/\|])(?=\s|[\!\.\?]|$)", "token_emote", text)
	with open("C:\data\\output.txt", "w") as output_file:
		output_file.write(text)