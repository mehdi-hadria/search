import os
import sys
import unittest
from unittest import mock

from test_data import *
from src.search_engine import InteractiveSearchEngine


class TestInteractiveSearchEngine(unittest.TestCase):

    @mock.patch('builtins.input')
    def test_start(self):
        self.assertEqual(1,1)



if __name__ == '__main__':
    unittest.main()
