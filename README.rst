============
Page counter
============

Hello! This is small Python library and commandline tool to count number of standard pages in the
text, files and folders. Comes with common standard page dialects builtin, but is super easy to
define your very own method of page counting.

Standard page is primary good unit of text length because it's doesn't take into account any
formatting but the text itself only. It's useful e.g. when you want to know how much pages you wrote
and how much will you get pay. Standard pages are used among book authors and publishers,
translators and their clients, in newspaper world and many other areas.

Page Counter can be used as Python library called ``page_counter``, or easy-to-use commandline tool
called ``page-counter``.

Installation
************

Installation will bring on your computer the both - library and commandline tool. Page Counter requires Python 3 installed. Then install it in standard Python way with

::

   pip install page-counter

Page Counter as Python Library
******************************

Page Counter as API has two parts: ``PageCounter`` class and functions called standard page dialects that does page counting itself dialects.

``PageCounter()`` class has only one required parameter: text to analyse::

   page_counter = PageCounter("There were froggies by the lake, "
                              "they were thinking what to make.")

Second only ``PageCounter``\`s parameter is optional flag to clean out HTML tags from the text. This
is disabled by default but if you pass for example ``<p class="intro">sometext</p>`` it will use
``sometext`` as text to analyse::

   page_counter = PageCounter("<p class="verse">There were froggies by the lake, "
                              "they were thinking what to make.</p>", strip_html=True)

There are only four intuitive methods of ``PageCounter`` instance:

* ``chars_with_spaces()`` says number of characters including space character
* ``chars_without_spaces()`` says number of characters except for space character
* ``word_count()`` says number of words
* ``page_count(dialect)`` says how many pages has the text computed using specified standard page dialect.

All methods returns integer number. ``page_count()`` called with builtin dialect never returns zero
pages - even one word or one letter long text is at least one page. Your custom dialects may behave
differently.

Standard page dialects
======================

There is no universally accepted standard page. You easily come across different dialects based on
country, convention or organization-specific. PageCounter is ready for this variability. As a
parameter to ``page_count()`` you must specify *some* page dialect. Dialect argument may be of str
for builtin dialects, or of callable for your own dialects.

If argument is of str, it must be builtin dialect name. Builtin dialect names are defined in
``page_counter.dialect_names`` list. For example::

   number_of_pages = page_counter.page_count('cz_sk_1800_chars_space_savvy_standard_page')

Or you can write your own dialect callable (i.e. a function for our purposes) and pass it to
``page_count()``. Your dialect function must accept ``PageCounter`` instance. Use ``PageCounter``
methods to compute page count. Example of simple dialect function::

   def my_company_page_standard(page_counter):
     return page_counter.chars_with_spaces // 1500

   number_of_pages = page_counter.page_count(my_company_page_standard)

If you think your standard page dialects should be builtin dialect, consider sharing it as an issue
or (better) as a pull request.

Builtin standard page dialects
==============================

Currently PageCounter includes the following builtin page dialects.

* ``cz_sk_1800_chars_standard_page`` - Czech and Slovak standard page (normostrana) is 1800 chars per page including spaces.
* ``cz_sk_1800_chars_space_savvy_standard_page`` - Czech and Slovak standard page (normostrana) is 1800 chars per page excluding multiple spaces.
* ``uk_1000_words_standard_page`` - UK standard page is 1000 words per page.
* ``eu_1500_chars_standard_page`` - Standard page used in many EU countries is 1500 chars per page including spaces.
* ``eu_1500_chars_space_savvy_standard_page`` - Standard page used in many EU countries is 1500 chars per page excluding multiple spaces.

Page Counter commandline tool
*****************************

By installing PageCounter you will also get handy commandline tool ``page-counter`` for page count
detection in single file or files in a folder. Usage::

   page-counter <dialect> <file>
   page-counter <dialect> <folder> <file_extension>

For example to count pages in ``readme.rst`` in current directory using Czech standard page
dialect::

   page-counter cz_sk_1800_standard_pages readme.rst

For example to count pages recursively in all \*.txt or \*.TXT files in
``~/books/python-for-novices/``::

   page-counter cz_sk_1800_standard_pages ~/books/python-for-novices/ txt

If you execute ``page-counter`` without parameters or with invalid number of parameters, you will get list of known builtin standard page dialects.


Contributing
************
If you have something you'd like to contribute, the best approach is to send a well-formed pull
request, complete with tests and documentation, as needed. Pull requests should be focused: trying
to do more than one thing in a single request will make it more difficult to process.