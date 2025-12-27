import re
FILE_PATH = "src/exmpl.csv"
OUTPUT_PATH = "src/out.csv"
REGEX_PATTERN = r"\d\d.\d\d.\d\d\d\d"

def main():
    input_lines = []
    output_lines = []
    regex_matcher = re.compile(REGEX_PATTERN)

    # read in file
    with open(FILE_PATH, "r") as file:
        input_lines = file.readlines()
    
    # search file for pattern
    for line in input_lines:
        to_store = line
        for segment in line.split(";"):
            if regex_matcher.search(segment):
                to_store = to_store.replace(segment, convert_date(segment))
        output_lines.append(to_store)

    # write out changed file
    with open(OUTPUT_PATH, "w") as file:
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
    return f"{str(to_convert[6:10])}-{str(to_convert[3:5])}-{str(to_convert[:2])}"


if __name__ == "__main__":
    main()