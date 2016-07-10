import os
import shutil
import time

def make():

	files = os.listdir('src')

	basefile = open('templates/base.html', 'r')
	basehtml = basefile.read()
	basefile.close()

	for basepath, folders, files in os.walk('src'):
		relative_path = basepath[3:].strip(os.path.sep)
		dist_path = os.path.join('dist', relative_path)

		# make the folder if missing
		if not os.path.exists(dist_path):
			os.makedirs(dist_path)
			print 'made {0}'.format(dist_path)

		# make the html page
		for filename in files:
			if filename.endswith('.html'):
				sourcefile = open(os.path.join(basepath, filename), 'r')
				content = sourcefile.read()
				sourcefile.close()

				html = basehtml.format(content=content)

				targetfile = open(os.path.join(dist_path, filename), 'w')
				targetfile.write(html)
				targetfile.close()

				print 'updated {0}'.format(os.path.join(dist_path, filename))

		# copy images
		if relative_path=='images':
			for filename in files:
				shutil.copyfile(os.path.join(basepath, filename), os.path.join(dist_path, filename))
				print 'copied {0}'.format(os.path.join(dist_path, filename))

while True:
	make()
	time.sleep(2)