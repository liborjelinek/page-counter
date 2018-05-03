import os
from unittest import TestCase
from unittest.mock import MagicMock

from page_counter import PageCounter


class TestPageCounter(TestCase):
    @classmethod
    def setUpClass(cls):
        test_file_path = os.path.join('resources', 'test_text.txt')
        with open(test_file_path, 'r') as f:
            cls.test_text = f.read()

    def test_chars_with_space(self):
        expected = 8216
        actual = PageCounter(self.test_text).chars_with_spaces()

        self.assertEqual(expected, actual)

    def test_chars_without_space(self):
        expected = 6569
        actual = PageCounter(self.test_text).chars_without_spaces()

        self.assertEqual(expected, actual)

    def test_word_count(self):
        expected = 1333
        actual = PageCounter(self.test_text).word_count()

        self.assertEqual(expected, actual)

    def test_strip_html(self):
        html = '<p class="intro">sometext</p>'
        actual = PageCounter(html, strip_html=True).text
        expected = 'sometext'
        self.assertEqual(expected, actual)

    def test_page_count_str_dialect_must_be_builtin(self):
        """
        Tests that if ``dialect`` argument passed to ``page_count()`` is string, it must be one of
        builtin dialect names.
        """
        with self.assertRaises(ValueError):
            PageCounter('some text').page_count('non_existing_builtin_dialect')

    def test_page_count_dialect_is_not_str_or_callable(self):
        """
        Tests that ``dialect`` argument isn't str or callable, an TypeError is raised.
        """
        with self.assertRaises(TypeError):
            PageCounter('some text').page_count(3.14)  # float passed

    def test_page_count_dialect_as_callable(self):
        """
        Tests that if ``dialect`` argument is callable, it's really called.
        """
        mock_dialect = MagicMock()
        PageCounter('some text').page_count(mock_dialect)
        mock_dialect.assert_called()
