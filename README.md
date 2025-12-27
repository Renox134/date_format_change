# Date Format Swap Utility

A small command-line utility that scans a CSV-like file for date strings and converts them from `DD/MM/YYYY` (or similar) to the ISO format `YYYY-MM-DD`.

The tool is flexible enough to handle different date separators and allows custom input/output paths and regex patterns.

---

## What it does

* Reads a text/CSV-like file (semicolon-separated by default)
* Finds date strings matching a configurable regex
* Converts matched dates from `DD/MM/YYYY` → `YYYY-MM-DD`
* Writes the transformed content to a new output file

---

## Requirements

* Python 3.8+
* No external dependencies (standard library only)

---

## Usage

Run the script from the command line:

```bash
python main.py
```

By default, it will:

* Read from: `src/input.csv`
* Write to: `src/out.csv`
* Match dates using the regex: `\d\d.\d\d.\d\d\d\d`

---

## Command-line options

| Option           | Description                          | Default              |
| ---------------- | ------------------------------------ | -------------------- |
| `-f`, `--file`   | Path to the input file               | `src/input.csv`      |
| `-o`, `--output` | Path to the output file              | `src/out.csv`        |
| `-r`, `--regex`  | Regex pattern used to identify dates | `\d\d.\d\d.\d\d\d\d` |

### Example

```bash
python main.py -f data/raw.csv -o data/converted.csv
```

Using a custom regex (e.g. dots instead of slashes):

```bash
python main.py -r "\d\d\.\d\d\.\d\d\d\d"
```

---

## Bonus Hint
To confirm that nothing was changed that shouldn't have been, you can use a file compare checker like the one accessible at https://www.diffchecker.com/text-compare/

## Notes & Limitations

* The tool assumes dates are in `DD/MM/YYYY` order internally.
* The separator character does **not** matter (`/`, `.`, `-`, etc.), as long as the regex matches.
* Files are processed line by line and split on semicolons (`;`).
* No validation is performed on date correctness (e.g. `32/13/2023`).

---

## License

MIT
