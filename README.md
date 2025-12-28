# CSV Date Converter

A small command-line tool that scans a CSV-like file for date values and converts them into ISO format (`YYYY-MM-DD`).

It’s designed for simple, delimiter-based files (not strict RFC CSV parsing) and is especially useful when dates are embedded in larger datasets.

---

## Features

* Converts dates like `DD/MM/YYYY`, `DD.MM.YYYY`, `DD-MM-YYYY`, etc. to `YYYY-MM-DD`
* Supports different date layouts via a format flag
* Works on any CSV-like file with a configurable cell separator
* Preserves all non-date content unchanged

---

## Requirements

* Python 3.10+ (uses `match` / `case`)
* No external dependencies

---

## Usage

```bash
python main.py [options]
```

### Options

| Flag | Long form       | Description               | Default         |
| ---- | --------------- | ------------------------- | --------------- |
| `-f` | `--file`        | Input file path           | `src/input.csv` |
| `-o` | `--output`      | Output file path          | `src/out.csv`   |
| `-d` | `--date_format` | Date format to search for | `DD.MM.YYYY`    |
| `-s` | `--separator`   | Cell separator character  | `;`             |

---

## Date Format Syntax

The `--date_format` option defines how dates appear in the input file.

* `D`, `M`, `Y` represent digits
* `.` means *any separator character* (`/`, `.`, `-`, etc.)

### Supported formats

* `DD.MM.YYYY`
* `YYYY.MM.DD`

### Examples

| Input        | Format       | Output       |
| ------------ | ------------ | ------------ |
| `31/12/2023` | `DD.MM.YYYY` | `2023-12-31` |
| `31.12.2023` | `DD.MM.YYYY` | `2023-12-31` |
| `2023-12-31` | `YYYY.MM.DD` | `2023-12-31` |

---

## Examples

```bash
python main.py \
  --file data/input.csv \
  --output data/output.csv \
  --date_format DD.MM.YYYY \
  --separator ";"
```

This will scan each cell of the input file, find matching dates, convert them, and write the result to the output file.

While this was done in the example, **the input and output files don't have to be specified**. By default, the tool will take the input from **input.csv**, and will write the output to **output.csv** (both located in the projects source folder).

---

## Bonus Hint
To confirm that nothing was changed that shouldn't have been, you can use a file compare checker like the one accessible at https://www.diffchecker.com/text-compare/

---

## Notes & Limitations

* This is **not a full CSV parser** (quoted fields, escaped separators, etc. are not handled).
* Only the two date formats listed above are supported.
* Dates are detected using regular expressions; malformed dates may still be converted if they match the pattern.

---

## License

MIT (or whatever you prefer)
