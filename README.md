### One-liner description:
A Python script that performs a dictionary-based brute-force attack on a ZIP file to crack its password using multithreading for faster execution.

### README.md:

```markdown
# ZIP Password Cracker

This Python script uses a dictionary-based brute-force attack with multithreading to crack the password of a ZIP file. It attempts each word from the provided dictionary file and extracts the ZIP file when the correct password is found.

## Features:
- Multithreaded brute-force password cracking
- Colored output for easier identification of successful cracks
- Simple usage with `optparse` for command-line argument parsing

## Usage:

```bash
python zip_cracker.py -f <zipfile> -d <dictionary file>
```

### Options:
- `-f` : Path to the ZIP file you want to crack
- `-d` : Path to the dictionary file containing potential passwords (one per line)

## Requirements:
- `termcolor` for colored output
- Python 3.x

## Example:

```bash
python zip_cracker.py -f secret.zip -d /path/to/dictionary.txt
```

## License:
MIT License
```

This README provides a clear, concise overview of how to use the script, its functionality, and necessary dependencies.
