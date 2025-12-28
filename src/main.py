import re
import argparse

DEFAULT_INPUT_PATH = "src/input.csv"
DEFAULT_OUTPUT_PATH = "src/out.csv"
DEFAULT_DATE_FORMAT = "DD%MM%YYYY"


def build_arg_parser() -> argparse.ArgumentParser:
    """
    Builds and returns the argument parser for the command line tool.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Searches a CSV-like file for date patterns and converts them "
            "from DD/MM/YYYY (or similar) to YYYY-MM-DD."
        )
    )

    parser.add_argument(
        "-f", "--file",
        default=DEFAULT_INPUT_PATH,
        help="Path to the input file (default: src/exmpl.csv)"
    )

    parser.add_argument(
        "-o", "--output",
        default=DEFAULT_OUTPUT_PATH,
        help="Path to the output file (default: src/out.csv)"
    )

    parser.add_argument(
        "-d", "--date_format",
        default=DEFAULT_DATE_FORMAT,
        help=(
            "Date format of the entries that should be changed. The '%' character means that any separator (e.g. ./-,) is allowed."
            "(default: DD%MM%YYYY"
        )
    )

    return parser


def main():
    parser = build_arg_parser()
    args = parser.parse_args()

    input_lines = []
    output_lines = []
    regex_matcher = re.compile(date_format_to_regex(args.date_format))

    # read in file
    with open(args.file, "r") as file:
        input_lines = file.readlines()

    # search file for pattern
    for line in input_lines:
        to_store = line
        for segment in line.split(";"):
            to_replace = regex_matcher.search(segment)
            if to_replace is not None:
                to_store = to_store.replace(to_replace.group(), convert_date(to_replace.group(),
                                                                             args.date_format))
        output_lines.append(to_store)

    # write out changed file
    with open(args.output, "w") as file:
        file.writelines(output_lines)


def convert_date(to_convert: str, format: str) -> str:
    """
    Expects a date of type DD%MM%YYYY or YYYY%MM%DD and transforms it into a
    date of type YYYY-MM-DD.
    The separation character of the input doesn't matter.

    :param to_convert: The date of type DD/MM/YYYY to convert.
    :type to_convert: str
    :param format: The date format, either DD%MM%YYYY or YYYY%MM%DD.
    :type format: str
    :return: The date, formated in YYYY-MM-DD.
    :rtype: str
    """
    match format:
        case "DD%MM%YYYY":
            return f"{to_convert[6:10]}-{to_convert[3:5]}-{to_convert[:2]}"
        case "YYYY%MM%DD":
            return f"{to_convert[:4]}-{to_convert[5:7]}-{to_convert[8:]}"
        case _:
            raise ValueError("The provided date format was not recognized. Valid date formats are DD%MM%YYYY or YYYY%MM%DD.")


def date_format_to_regex(date_format: str) -> str:
    """
    Creates a matching regex for a given date format.
    
    :param date_format: The date format of which the regex should be created.
    :type date_format: str
    :return: The correctly formated regex.
    :rtype: str
    """
    r = r""
    for char in date_format:
        match char:
            case "D" | "M" | "Y":
                r += r"\d"
            case "%" | ".":
                r += r"."
            case _:
                r += char
    
    return r


if __name__ == "__main__":
    main()
