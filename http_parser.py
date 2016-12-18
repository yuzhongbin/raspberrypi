import HTMLParser
import urllib
import sys

url = "http://www.baidu.com"

class parseLinks(HTMLParser.HTMLParser):
	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for name, value in attrs:
				if name == 'href':
					print 'name_value: ', value
					print 'first tag:', self.get_starttag_text()
					print '\n'

def main():
	parser = parseLinks()
	parser.feed(urllib.urlopen(url).read())	
	parser.close()

if __name__ == "__main__":
	main()