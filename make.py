import os

files = os.listdir('src')

basefile = open('templates/base.html', 'r')
basehtml = basefile.read()
basefile.close()

for filename in files:
	sourcefile = open('src/' + filename, 'r')
	content = sourcefile.read()
	sourcefile.close()

	html = basehtml.format(content=content)

	targetfile = open('dist/' + filename, 'w')
	targetfile.write(html)
	targetfile.close()

	print filename