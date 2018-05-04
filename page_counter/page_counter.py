import re

from bs4 import BeautifulSoup

from page_counter import dialect_names, dialects


class PageCounter:
    """
    Standard page counter.
    """

    def __init__(self, text, strip_html=False):
        """

        :param text:
        :param strip_html: Clean out HTML from ``text``. For example from
            ``<p class="intro">sometext</p>`` makes ``sometext``.
        """
        self.text = text

        if strip_html:
            # dear BeautifulSoup, use builtin Python HTML parser
            self.text = BeautifulSoup(text, 'html.parser').get_text()

    def chars_with_spaces(self):
        return len(self.text)

    def chars_without_spaces(self):
        counter = 0
        for ch in self.text:
            if not ch.isspace():
                counter += 1

        return counter

    def word_count(self):
        return len(re.findall(r'\w+', self.text))

    def page_count(self, dialect):
        """
        Says how many pages has the text computed using specified standard page dialect.

        :param dialect: Accepts str or callable.

            If argument is of str, it must be builtin dialect name. Existing dialect names are
            defined in ``page_counter.dialect_names`` list.

            If argument is of callable, it must accept ``PageCounter`` instance as its only
            parameter. Use ``PageCounter`` methods to compute page count. Example of simple
            dialect function::

                def my_company_page_standard(page_counter):
                    return page_counter.chars_with_spaces // 1800

        :return: Number of pages computed using specified dialect.
        """
        if isinstance(dialect, str):
            if dialect not in dialect_names:
                raise ValueError(
                    "Unknown builtin dialect '{dialect}'. If you pass 'dialect' argument of a "
                    "str type, it must be one of builtin dialect names. Existing builtin names are "
                    "defined in 'page_counter.dialect_names' list and contains these dialect"
                    "names: {dialect_names}".format(dialect=dialect, dialect_names=dialect_names))

            # Lookup in "dialects" module function of specified name
            dialect_function = getattr(dialects, dialect)
            return dialect_function(self)

        if callable(dialect):
            return dialect(self)

        raise TypeError("Passed 'dialect' argument must be of a str or callable, but received "
                        "'{type}' type.".format(type=dialect.__class__.__name__))
