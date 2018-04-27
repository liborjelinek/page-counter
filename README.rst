=====================
Standard page counter
=====================

Hello! This is small Python library to count number of standard pages in the text. Common standard page dialects builtin, easy to plugin custom definition. Useful when want to know how much pages have some text, how many will you pay or be paid etc.

Contributing
************
If you have something you'd like to contribute, the best approach is to send a well-formed pull request, complete with tests and documentation, as needed. Pull requests should be focused: trying to do more than one thing in a single request will make it more difficult to process.

If you have a bug or feature request you can try logging an issue.

There's no harm in creating an issue and then submitting a pull request to resolve it. This can be a good way to start a conversation and can serve as an anchor point.

.. Development
   ***********
   To get set up for development, activate your virtualenv and use pip to install from requirements-dev.txt:

   $ pip install -r requirements-dev.txt
   To run the tests:

   $ django-admin test --settings tests.settings
   To run the full test suite in a range of environments, run tox from the root of the project:

   $ tox
   This includes some static analysis to detect potential runtime errors and style issues.
