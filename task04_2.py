import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('logger')

path = '.'
files = os.listdir(path)

for f in files:
	print(f)

logger.info(f'Текущий каталог: {str(os.getcwd())}')
logger.info(f'Обработано {str(len(files))} файлов')


