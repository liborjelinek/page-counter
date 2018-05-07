import os
import sys

from page_counter import PageCounter, dialect_choices

RT_INVALID_USAGE = -1


def print_err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def invalid_usage():
    print_err("Missing commandline arguments. You must always specify standard page dialect and "
              "file or folder. For folder you have to say which files you want to explore.")
    print_err()
    print_err("    page-counter <dialect> <file>")
    print_err("    page-counter <dialect> <folder> <file_extension>")
    print_err()
    print_err("For example to count pages in readme.rst in current directory using Czech standard "
              "page dialect:")
    print_err()
    print_err("    page-counter cz_sk_1800_standard_pages readme.rst")
    print_err()
    print_err("For example to count pages in all *.txt or .TXT files in ~/books/python-for-novices/"
              ":")
    print_err()
    print_err("    page-counter cz_sk_1800_standard_pages ~/books/python-for-novices/ txt")
    print_err()
    print_err("Dialects known to page-counter are:")

    for (dialect_name, dialect_help) in dialect_choices:
        print_err("    * {} - {}".format(dialect_name, dialect_help))

    return RT_INVALID_USAGE


def in_folder(argv):
    dialect = argv[0]
    folder = argv[1]
    ext = argv[2]

    total_pages = 0

    print("Counting pages in *.{ext} files in '{folder}' using '{dialect}' dialect:".format(
        ext=ext, folder=folder, dialect=dialect))

    def walk_error(error):
        print_err("Encountered '{error}' during traversing folder".format(error=error))

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
        print("-> {total_pages} total pages in '{dialect}' dialect.".format(total_pages=total_pages,
                                                                            dialect=dialect))

    return total_pages


def in_file(argv):
    dialect = argv[0]
    file = argv[1]

    with open(file, 'r') as f:
        text = f.read()
        pages = PageCounter(text).page_count(dialect)

    print("File '{file}' has {pages} pages using '{dialect}' dialect.".format(file=file,
                                                                              pages=pages,
                                                                              dialect=dialect))
    return pages


def main(argv=sys.argv[1:]):
    num_of_args = len(argv)

    # return code is page count

    if num_of_args == 2:
        return in_file(argv)

    elif num_of_args == 3:
        return in_folder(argv)

    else:
        return invalid_usage()


if __name__ == '__main__':
    sys.exit(main())
