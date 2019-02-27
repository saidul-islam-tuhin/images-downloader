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
		raise FileNotFoundError(e)
	
	except Exception as e:
		logger.error(e)

	return urls


def image_downloader_func(input_file_path='', save_images_path=''):
	"""
	Download image in JPEG format from given links.

	:param input_file_path: Text file path where image link stored
	:param output_file_path: Folder path where downloaded image will be saved.
	"""

	if input_file_path:
		input_file_path = Path(input_file_path)
	else:
		input_file_path = Path.cwd().joinpath('images.txt')


	if save_images_path:
		save_images_path = Path(save_images_path)
	else:
		save_images_path = Path.cwd().joinpath('Images')
		

	image_urls = file_read(input_file_path)


	if image_urls:
		total_urls = len(image_urls)

		try:
			save_images_path.mkdir(exist_ok=True)
		
		except OSError as e:
			logger.error(e)

		for count, link in enumerate(image_urls, 1):
			try:
				img_req = requests.get(link, allow_redirects=False, timeout=(5,15))
				
				if img_req.status_code == 200:	
					img_req.raw.decode_content = True
					buffer_content = io.BytesIO(img_req.content) # IMPORTANT: Convert byte stream before passing Image.open()
					img = Image.open(buffer_content)

					img_file_name = Path(link).stem + '.jpeg'
					img_full_path = save_images_path.joinpath(img_file_name)

					img.save(img_full_path)
					logger.debug("Download and save image:{}; Remain: {}".format(img_file_name,total_urls-count))

				else:
					logger.error("URL:{} > Response Code: {}".format(link,img_req.status_code))
			
			except (ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError) as img_req_e:
				logger.error(img_req_e)
			
			except Exception as e:
				logger.error(e)
	
	else:
		logger.debug("No image url found in {}".format(input_file_path))


if __name__ == '__main__':
	
	image_downloader_func()
