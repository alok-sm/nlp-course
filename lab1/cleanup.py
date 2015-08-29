import re

def cleanup(text):

	text = text.lower().replace("rt", "").replace("&amp;", "&")
	text = re.sub(r"#[^ \n\t]*", "token_hash", text)
	text = re.sub(r"@[^ \n\t]*", "token_handle", text)
	text = re.sub(r"(mailto\:|(news|(ht|f)tp(s?))\://)[^ \n\t]*" , "token_url", text)
	text = re.sub(r"(\:\w+\:|\<[\/\\]?3|[\(\)\\\D|\*\$][\-\^]?[\:\;\=]|[\:\;\=B8][\-\^]?[3DOPp\@\$\*\\\)\(\/\|])(?=\s|[\!\.\?]|$)", "", text)

	emoji_regex = re.compile(u'['
		u'\U0001F300-\U0001F64F'
		u'\U0001F680-\U0001F6FF'
		u'\u2600-\u26FF\u2700-\u27BF]+', 
		re.UNICODE
	)

	text = emoji_regex.sub('', text)

	return text