import sys
import os
import unittest
from unittest import mock

from src.helpers import get_all_text_files, read_unique_words,get_commons_words
from test_data import *


class TestGetAlTextFiles(unittest.TestCase):

    @mock.patch('os.listdir')
    def test_get_text_files_is_ok(self, mock_listdir):
        mock_listdir.return_value = ['a.json', 'b.json', 'c.json', 'd.txt']
        files = get_all_text_files('.')
        self.assertEqual(1, len(files))

    @mock.patch('os.listdir')
    def test_get_text_files_not_found(self, mock_listdir):
        mock_listdir.return_value = ['a.json', 'b.json', 'c.json', ]
        files = get_all_text_files('.')
        self.assertEqual(0, len(files))

    @mock.patch('os.listdir')
    def test_get_text_files_raise_not_directory_exception(self, mock_listdir):
        mock_listdir.return_value = ['a.json', 'b.json', 'c.json', ]
        with self.assertRaises(ValueError) as exc:
            files = get_all_text_files('test.json')

class TestReadUniqueWords(unittest.TestCase):

    @mock.patch("builtins.open", mock.mock_open(read_data=file_content))
    def test_read_unique_words_is_ok(self):

        words = read_unique_words("fichier.txt")
        self.assertIn('file_name', words)
        self.assertIn('unique_words', words)
        self.assertEqual(words['file_name'],read_unique_expected_output['file_name'])
        #self.assertSetEqual(words['unique_words'],read_unique_expected_output['unique_words'])

    def test_get_commons_words(self):

        result= get_commons_words(test_get_commons_words['set_words'],test_get_commons_words['words_to_match'])
        self.assertEqual(result,test_get_commons_words['expected_rate'])



if __name__ == '__main__':
    unittest.main()

