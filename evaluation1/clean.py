import re
f = open("C:\data\\twit.txt", 'r')	#Input File
text = f.read()
text = re.sub(r"#[^ \n\t]*", "token_hash", text)
text = re.sub(r"@[^ \n\t]*", "token_handle", text)
text = re.sub(r"(mailto\:|(news|(ht|f)tp(s?))\://)[^ \n\t]*" , "token_url", text)
f1 = open("C:\data\\try.txt", "w")	#Output File
f1.write(text)
f.close()
f1.close()