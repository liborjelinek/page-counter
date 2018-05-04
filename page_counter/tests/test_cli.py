import os
from unittest import TestCase

from page_counter import cli


class TestCli(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_file_path = os.path.join('resources', 'test_text.txt')
        with open(cls.test_file_path, 'r') as f:
            cls.test_text = f.read()

    def test_invalid_usage(self):
        # first arg is program itself
        self.assertEqual(cli.main(['']), cli.RT_INVALID_USAGE)    # no args
        self.assertEqual(cli.main(['', 'only_one_arg']), cli.RT_INVALID_USAGE)
        self.assertEqual(cli.main(['', 'more', 'than', 'three', 'args']), cli.RT_INVALID_USAGE)

    def test_in_folder(self):
        self.assertEqual(cli.main(['', 'cz_sk_1800_standard_page', 'resources', 'txt']), 5)

    def test_in_file(self):
        self.assertEqual(cli.main(['', 'cz_sk_1800_standard_page', self.test_file_path]), 5)
