import io
import os
import logging
from pathlib import Path

import requests
from PIL import Image

from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError


LOG_FORMAT = "%(levelname)s >  Line:%(lineno)s - %(message)s"
logging.basicConfig(filename="debug.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode="w",
                    )
logger = logging.getLogger(__name__)



def file_read(file_path):
	"""
	Read all link in line by line from file.

	:param file_path: File path which is instance of Path class
	:type file_path : Instance of Path class
	:returns: List of image download url
	:rtype: list
	"""
	
	urls = list()

	try:
		with file_path.open('r') as f:
			urls = f.read().splitlines()
	
	except (OSError, IOError) as e:
		logger.error(e)
	
	except Exception as e:
		print(type(e).__name__)
		logger.error(e)

	return urls

if __name__ == '__main__':
	
	image_downloader_func()