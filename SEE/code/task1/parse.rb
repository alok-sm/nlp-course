require "nokogiri"
require "json"

Dir.foreach("../../data") do |filename|
	data = {}
	comments = []
	next if filename == "." or filename == ".."
	doc = File.open("../../data/" + filename) do |datafile| 
		html = Nokogiri::HTML(datafile)
		html.css('#commInnings div .commentary-event').each do |element|
			element.css('.commentary-overs').map {|x| x.text}
			.zip(element.css('.commentary-text p').map {|x| x.text.split("\t").join("").split("\r")})
			.each do |ball|
				data[ball[0]] = ball[1].map {|y| y.gsub(/\,$/, '')}
				comments.insert(0, ball[1].join(' '))
			end
		end
	end
	File.open('../../json/' + filename.split('.')[0..-2].join('.') + '.json', 'w') { |file| file.write(JSON.dump(data)) }
	File.open('../../text/' + filename.split('.')[0..-2].join('.') + '.txt', 'w') { |file| file.write(comments.join("\n")) }
end

Dir.foreach("../../data") do |filename|
	next if filename == "." or filename == ".."
	doc = File.open("../../data/" + filename) do |datafile| 
		html = Nokogiri::HTML(datafile)
		wickets = html.css('.commentary-text p b')
		wickets = wickets.select { |element| /.*SR\: \d+\.\d+/.match(element) }.map { |element| element.text}
		File.open('../../scoreboard/' + filename.split('.')[0..-2].join('.') + '.txt', 'w') { |file| file.write(wickets.join("\n")) }
	end
end
