import os
import my_music_app
import unittest
import tempfile


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        my_music_app.app.testing = True
        self.app = my_music_app.app.test_client()




if __name__ == '__main__':
    unittest.main()
