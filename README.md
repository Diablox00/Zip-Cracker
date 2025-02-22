# ZIP Password Cracker

This Python script uses a dictionary-based brute-force attack with multithreading to crack the password of a ZIP file. It attempts each word from the provided dictionary file and extracts the ZIP file when the correct password is found.

## Features:
- Multithreaded brute-force password cracking
- Colored output for easier identification of successful cracks
- Simple usage with `optparse` for command-line argument parsing

## Usage:

```bash
python zip_cracker.py -f <zipfile> -d <dictionary file>
