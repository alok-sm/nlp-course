def convert(x):
	try:
		x = int(x)
		if(x not in [0, 1]):
			raise Exception()
	except Exception, e:
		raise Exception()
	return x

def get_comments_fvs():
	comments = []
	fvs = []
	with open('dataset_final.csv') as fp:
		for line in fp:

			line = line.split('"')
			if(len(line) != 3):
				continue
			try:
				fv = [convert(x) for x in line[2].split(',')[1:]]
			except:
				continue

			comment = line[1].split(',')


			if(len(comment) < 3):
				continue


			if(len(fv) != 22):
				continue

			comments.append([comment[0].strip(), comment[1].strip(), ','.join(comment[2:]).strip()])
			fvs.append(fv)

	return comments, fvs
