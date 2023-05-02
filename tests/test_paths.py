import unittest
import os
import sys

sys.path.append(os.path.join(os.getcwd(), 'src/app'))
sys.path.append(os.path.join(os.getcwd(), 'src/'))

from widgets_handlers import get_path_to_images

class TestPathsArea(unittest.TestCase):

    def test_path_to_images(self):
        current_dir = os.getcwd()
        parent_dir = os.path.dirname(current_dir)
        images = os.path.join(parent_dir, 'images/icons')
        self.assertEquals(get_path_to_images(), images)

    def test_path_to_images_type(self):
        self.assertEquals(type(get_path_to_images()), str)


if __name__ == "__main__":
    unittest.main()
