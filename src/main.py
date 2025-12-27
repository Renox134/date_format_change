import re
import argparse

DEFAULT_INPUT_PATH = "src/input.csv"
DEFAULT_OUTPUT_PATH = "src/out.csv"
DEFAULT_REGEX_PATTERN = r"\d\d.\d\d.\d\d\d\d"


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
        "-r", "--regex",
        default=DEFAULT_REGEX_PATTERN,
        help=(
            "Regex pattern used to identify dates "
            "(default: \\d\\d.\\d\\d.\\d\\d\\d\\d)"
        )
    )

    return parser


def main():
    parser = build_arg_parser()
    args = parser.parse_args()

    input_lines = []
    output_lines = []
    regex_matcher = re.compile(args.regex)

    # read in file
    with open(args.file, "r") as file:
        input_lines = file.readlines()

    # search file for pattern
    for line in input_lines:
        to_store = line
        for segment in line.split(";"):
            if regex_matcher.search(segment):
                to_store = to_store.replace(segment, convert_date(segment))
        output_lines.append(to_store)

    # write out changed file
    with open(args.output, "w") as file:
        file.writelines(output_lines)


def convert_date(to_convert: str) -> str:
    """
    Expects a date of type DD/MM/YYYY and transforms it into a
    date of type YYYY-MM-DD.
    The separation character of the input doesn't matter.

    :param to_convert: The date of type DD/MM/YYYY to convert.
    :type to_convert: str
    :return: The converted date of type YYYY-MM-DD
    :rtype: str
    """
    return f"{to_convert[6:10]}-{to_convert[3:5]}-{to_convert[:2]}"


if __name__ == "__main__":
    main()
