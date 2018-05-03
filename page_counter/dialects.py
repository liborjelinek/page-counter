"""
Page dialect definitions.

YOUR PAGE DIALECT CONTRIBUTION WELCOMED! Dialects are defined as functions accepting ``PageCounter``
instance. Function name and docstring is important because it will be used as dialect name and
dialect description in ``page-counter`` CLI tool and elsewhere. For example::

   def one_word_two_page(page_counter):
       \"\"\"Example of crazy page dialect that counts one word as two page\"\"\"
       return page_counter.word_count() * 2

Because a lot of page definitions are very similar except page size (characters per page) we provide
two helper functions - plain standard pages and "space savvy" standard pages that reduce multiple
spaces in the text. It's a good practice to provide both variants of every page standard dialect.

Finally write tests in ``page_counter.tests.test_dialects`` and submit pull request.
"""


# ################
# Helper functions
# ################


def _plain_standard_page(page_counter, chars_per_page):
    """
    Plain standard pages.

    This dialect counts page number as *<chars_with_spaces> / <chars_per_size>*.

    Properly round to integer number for humans. Always returns at least 1 or more.

    :param page_counter: ``PageCounter`` instance
    :param chars_per_page: how many characters has a page
    :return: number of pages
    """
    length = page_counter.chars_with_spaces()
    pages = round(length / chars_per_page)

    if pages == 0:
        return 1

    return pages


def _space_savvy_standard_page(page_counter, chars_per_page):
    """
    Standard page excluding multiple spaces.

    This dialect reduce extra spaces by counting page number as *<chars_without_spaces> +
    <word_count>*. Therefore every word boundary is treated as single space only.

    Space-savvy counting is suited for technical documentation, programming texts, markup languages
    like reStructuredText or Markdown. They typically contain a lot of space characters just as
    indentation or formatting etc.

    Properly round to integer number for humans. Always returns at least 1 or more.

    :param page_counter: ``PageCounter`` instance
    :param chars_per_page: how many characters has a page
    :return: number of pages
    """
    length = page_counter.chars_without_spaces() + page_counter.word_count()
    pages = round(length / chars_per_page)

    if pages == 0:
        return 1

    return pages


# ####################################
# Actual dialect functions come bellow
# ####################################

def cz_sk_1800_standard_page(page_counter):
    """
    Czech and Slovak standard page (normostrana) is 1800 chars per page including spaces.
    """
    return _plain_standard_page(page_counter, 1800)


def cz_sk_1800_space_savvy_standard_page(page_counter):
    """
    Czech and Slovak standard page (normostrana) is 1800 chars per page excluding multiple spaces.
    """
    return _space_savvy_standard_page(page_counter, 1800)


# ####################################################
# Don't forget to append your dialects to builtin ones
# ####################################################

# Sequence of builtin dialects. For book-keeping purposes only. It contains 2-tuples of dialect
# name and description.
dialect_choices = (
    (cz_sk_1800_standard_page.__name__,
     cz_sk_1800_standard_page.__doc__.strip()),

    (cz_sk_1800_space_savvy_standard_page.__name__,
     cz_sk_1800_space_savvy_standard_page.__doc__.strip())
)

# Builtin dialect names list
dialect_names = [choice[0] for choice in dialect_choices]
