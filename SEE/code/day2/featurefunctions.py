def create_fn(keywords, index):
	def fn(comment):
		return int(
			sum([kw in ( comment + [""]*3 )[:3][index].lower() for kw in keywords]) > 0
		)
	return fn

def get_functions():

	keywords_1 = [
		["out"], 
		["no run"], 
		["four", "4"], 
		["six", "6"], 
		["wide"],
		["no ball"], 
		["leg bye"],
	]

	keywords_2 = [
		# ["out"],
		# ["no run"],
		# ["four", "4"],
		# ["six","6"],
		# ["wide"],
		["no-ball", "no ball"],
		# ["leg bye"],
		# ["mid"],
		# ["cover"],
		# ["slow"],
		# ["pace"],
		# ["quick"],
		# ["single"],
		# ["double"],
		# ["long"],
		# ["short"],
		# ["full"],
		# ["appeal"],
		["wicketkeeper", "keeper"],
		# ["spin"],
		# ["swing"],
		# ["fast"],
		# ["sweep"],
		# ["swept"],
		# ["scoop"],
		# ["couple"],
		# ["fine"],
		# ["leg"],
		# ["odd"]
		["defend", "defence", "block", "dot"],
		["left alone", "dot"],
		["beat", "dot", "miss"],
		["edge", "chip"],
		["caught", "catch", "take", "took"],
		["air"],
		["runout", "run out", "run-out"],
		["stump"],
		["leg before", "lbw", "plumb", "trapped"],
		# ["boundary"],
		# ["drive"],
		# ["stroke"],
		# ["pull"],
		["drop", "let down", "missed opportunity", "missed catch"],
		["stump"],
		["bouncer", "high", "short ball"],
		["yorker"],
		["overthrow"],
		["good fielding", "great fielding", "superb fielding", "fantastic fielding", "terrific fielding", "excellent fielding"],
		["free hit", "free-hit"],
		# ["high"],
		# ["distance"],
		# ["sledge"],
		# ["in"],
		# ["square"],
		# ["midwicket"],
		# ["wicket"],
		# ["hit"],
		# ["score"],
		# ["delivery"],
		# ["pitch"],
		# ["pad"],
		# ["glove"],
	]
	# print len([create_fn(keyword, 1) for keyword in keywords_1] + [create_fn(keyword, 2) for keyword in keywords_1 + keywords_2])
	return [create_fn(keyword, 1) for keyword in keywords_1] + [create_fn(keyword, 2) for keyword in keywords_1]