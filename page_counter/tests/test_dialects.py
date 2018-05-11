import os
from unittest import TestCase

from page_counter import PageCounter, dialect_names, dialects


class TestBuiltinDialects(TestCase):
    """
    Tests that are common for all dialect. Tests issued for every dialect from ``dialect_names``.
    """

    def test_dialect_return_1_at_min(self):
        """
        Tests that dialect callable returns 1 page count at minimum. For example one-letter
        text is still 1 page.
        """
        for dialect_name in dialect_names:
            with self.subTest(dialect_name=dialect_name):
                dialect = getattr(dialects, dialect_name)
                text = "There were froggies by the lake, they were thinking what to make."
                page_counter = PageCounter(text)

                self.assertEqual(1, page_counter.page_count(dialect),
                                 'Dialect "{dialect}" must return at least 1 page count at min'
                                 'even for few words only long text.'.format(dialect=dialect_name))


class TestCzSk1800StandardPages(TestCase):
    @classmethod
    def setUpClass(cls):
        test_file_path = os.path.join('resources', 'test_text.txt')
        with open(test_file_path, 'r') as f:
            cls.test_text = f.read()

    def test_cz_sk_1800_standard_page(self):
        expected = 5
        actual = PageCounter(self.test_text).page_count('cz_sk_1800_standard_page')

        self.assertEqual(expected, actual)

    def test_cz_sk_1800_space_savvy_standard_page(self):
        expected = 4
        actual = PageCounter(self.test_text).page_count('cz_sk_1800_space_savvy_standard_page')

        self.assertEqual(expected, actual)


class TestUk1000WordsStandardPage(TestCase):
    @classmethod
    def setUpClass(cls):
        test_file_path = os.path.join('resources', 'test_text.txt')
        with open(test_file_path, 'r') as f:
            cls.test_text = f.read()

    def test_uk_1000_words_standard_page(self):
        expected = 1
        actual = PageCounter(self.test_text).page_count('uk_1000_words_standard_page')

        self.assertEqual(expected, actual)


class TestEu1500CharsStandardPage(TestCase):
    @classmethod
    def setUpClass(cls):
        test_file_path = os.path.join('resources', 'test_text.txt')
        with open(test_file_path, 'r') as f:
            cls.test_text = f.read()

    def test_eu_1500_chars_standard_page(self):
        expected = 5
        actual = PageCounter(self.test_text).page_count('eu_1500_chars_standard_page')

        self.assertEqual(expected, actual)

    def test_eu_1500_chars_space_savvy_standard_page(self):
        expected = 5
        actual = PageCounter(self.test_text).page_count('eu_1500_chars_standard_page')

        self.assertEqual(expected, actual)