# Phone Lookup CLI Tool

A free and simple Python CLI tool to perform reverse phone number lookups using public data from NumLookup.com.

---

## Features

- Lookup a single phone number
- Bulk lookup from CSV file
- Outputs results to a CSV file
- Uses only free and public sources

---

## Demo

```bash
# Lookup one number
python lookup.py --number 1234567890

# Bulk lookup from input.csv and save to results.csv
python lookup.py --input input.csv --output results.csv
