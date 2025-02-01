import os
import unittest
from unittest.mock import patch
from pydub import AudioSegment
from create_voicemail import CreateVoicemail
from consts import CONSTS
from random import random
import uuid

class TestCreateVoicemail(unittest.TestCase):
    """
        Unit tests, not comprehensive (more coverage TBD).
        
        TO-DO:
            - Add tests for `generate_audio()`.
    """
    
    TEST_FILE_NAME = "test.mp3"
    TEST_NONEXIST_FILE_NAME = "dummy.mp3"
    TEST_DIR = f"TESTDIR_{uuid.uuid4()}"
    
    def setUp(self):
        """
            Setup: Create test directory. 
            
            This *assumes* that UUIDs are random.
        """
        os.mkdir(self.TEST_DIR)
        open(os.path.join(self.TEST_DIR, self.TEST_FILE_NAME), 'a').close()
        return super().setUp()
    
    def tearDown(self):
        """
            Teardown: somewhat unsafe way to remove test MP3 and test directory.
        """
        if os.path.isdir(self.TEST_DIR):
            if os.path.isfile(os.path.join(self.TEST_DIR, self.TEST_FILE_NAME)):
                os.remove(os.path.join(self.TEST_DIR, self.TEST_FILE_NAME))
            os.rmdir(self.TEST_DIR)
        return super().tearDown()
                     
    def test_get_safe_output_path_leading_slash(self):
        """
            Test leading slash stripping for get_safe_output_path().
        """
        expected = os.path.join(self.TEST_DIR, self.TEST_NONEXIST_FILE_NAME)
        path = CreateVoicemail.get_safe_output_path(
            self.TEST_NONEXIST_FILE_NAME,
            self.TEST_DIR + os.path.sep
        )
        self.assertEqual(path, expected)

    def test_get_safe_output_fakedir(self):
        """
            Test get_safe_output_path() for nonexistent paths.
        """
        with self.assertRaises(Exception) as ctx:
            CreateVoicemail.get_safe_output_path(
                self.TEST_FILE_NAME, 
                "random_fake_path"
            )
            self.assertIn("Output path does not exist.", str(ctx.exception))
            
    def test_get_safe_output_path_file_exists(self):
        """
            Test get_safe_output_path() for existing MP3.
        """
        with self.assertRaises(Exception) as ctx:
            CreateVoicemail.get_safe_output_path(
                self.TEST_FILE_NAME, 
                self.TEST_DIR
            )
            self.assertIn("File already exists.", str(ctx.exception))

if __name__ == "__main__":
    unittest.main()
