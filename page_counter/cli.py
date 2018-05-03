import os
import sys

from page_counter import PageCounter, dialect_choices


def _invalid_usage():
    print("""Missing commandline arguments. You must specify standard page dialect, folder, and
file type (extension). Usage:

    page-counter <extension> <folder> <dialect>

For example to count pages in all *.txt or .TXT files in ~/books/python-for-novices/ using Czech
standard page dialect:

    page-counter txt ~/books/python-for-novices/ cz_sk_1800_standard_pages

Dialects known to page-counter are:
""", file=sys.stderr)

    for (dialect_name, dialect_help) in dialect_choices:
        print("    * {} - {}".format(dialect_name, dialect_help), file=sys.stderr)


def walk_error(error):
    print("Encountered '{error}' during traversing folder".format(error=error),
          file=sys.stderr)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        _invalid_usage()
        sys.exit(1)

    ext = sys.argv[1]
    folder = sys.argv[2]
    dialect = sys.argv[3]

    total_pages = 0

    print("Counting pages in all {ext} files in '{folder}' using '{dialect}' "
          "dialect:".format(ext=ext, folder=folder, dialect=dialect))

    for dirpath, dirname, filenames in os.walk(folder, onerror=walk_error):
        for filename in filenames:
            if filename.lower().endswith('.' + ext):
                file_path = os.path.join(dirpath, filename)
                relative_file_path = os.path.relpath(file_path, folder)

                with open(file_path, 'r') as f:
                    text = f.read()
                    pages = PageCounter(text).page_count(dialect)
                    print("    * '{file}' file has {pages} pages".format(
                        file=relative_file_path, pages=pages))

                    total_pages += pages

    if total_pages == 0:
        print("No {ext} files found.")

    else:
        print("-> {total_pages} total pages in '{dialect}' dialect".format(total_pages=total_pages,
                                                                           dialect=dialect))
