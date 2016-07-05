import requests, os


def download():
	for fname in open('files.txt', 'r').read().splitlines():
		path = 'files/' + fname.split('.')[0] + '.html'

		if not os.path.exists(path):
			r = requests.get('http://shishuvan.com/' + fname)
			print fname
			open(path, 'w').write(r.content)

def clean():
	# clean header and footer
	for fname in os.listdir('files'):
		if fname.endswith('.html'):
			src = open('files/' + fname, 'r').read()

			if '<div id="content">' in src:
				src = src.split('<div id="content">', 1)[1]

			if '<div id="footer">' in src:
				src = src.split('<div id="footer">', 1)[0]

			open('files/' + fname, 'w').write(src)

if __name__=='__main__':
	#download()
	clean()