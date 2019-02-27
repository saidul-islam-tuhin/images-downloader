import os
import unittest
from pathlib import Path
from unittest.mock import mock_open, patch

import images_downloader



class ImageDownloaderTest(unittest.TestCase):

    def test_file_read(self):
        self.assertRaises(FileNotFoundError, images_downloader.file_read,"/home/user/not_exist.txt")
    

if __name__ == '__main__':
    unittest.main()