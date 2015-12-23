from lxml import etree
from lxml.etree import tostring
from itertools import chain
import os
import re
import json

DATA_PATH = '../../data/'
TEXT_PATH = '../../text/'
JSON_PATH = '../../json/'

comments = {}
comment_list = []

def get_text(nodes):
	if(type(nodes) != list):
		nodes = [nodes]
	ret = ''
	for node in nodes:
		parts = ([node.text] + list(chain(*([c.text, tostring(c), c.tail] for c in node.getchildren()))) + [node.tail])
		ret += ''.join(filter(None, parts))

	ret = re.sub(r'</*.*?>', '', ret)
	ret = re.sub(r'\&\#13\;', '', ret).strip()
	ret = ret.replace('\r', ' ')
	ret = ret.replace('\t', ' ')
	return ret


for html_filename in list(os.walk(DATA_PATH))[0][2]:
	text_filename = '.'.join(html_filename.split('.')[:-1])+'.txt'
	json_filename = '.'.join(html_filename.split('.')[:-1])+'.json'
	with open(DATA_PATH + html_filename, 'r') as html_file, open(TEXT_PATH + text_filename, 'w') as text_file, open(JSON_PATH + json_filename, 'w') as json_file:
		tree = etree.parse(html_file, parser = etree.HTMLParser())
		comment_elements = tree.xpath("id('commInnings')/div[2]/div[@class!='end-of-over-info']")
		for element in comment_elements:
			over_number = get_text(list(element.xpath("div[@class='commentary-overs']")))
			comment = get_text(list(element.xpath("div[@class='commentary-text']")))
			comment_list.append(comment)
			if(over_number != ""):
				comments[over_number] = {
					'text' : comment
				}

		text_file.write('\n'.join(comment_list))
		json.dump(comments, json_file)

