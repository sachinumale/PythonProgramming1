import os

import os
for dirpath,dirnames,filenames in os.walk('.'):
	print('Current Working Directory Path:',dirpath)
	print('Directories:',dirnames)
	print('Files:',filenames)
	print()
