import sys
import fgoogle
search = fgoogle.query().search("meh")
for item in search:
	print item['url']