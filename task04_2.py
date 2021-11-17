import os
import logging

logger = logging.getLogger('logger')
logger.info('info')
path = '.'
files = os.listdir(path)

for f in files:
	print(f)

