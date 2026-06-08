#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path

# Directory where this script is located
SCRIPT_DIR = Path(__file__).resolve().parent

# Input file containing LCSC part numbers (one per line)
LCSC_FILE = SCRIPT_DIR / "lcsc.txt"

# Output directory
OUTPUT_DIR = SCRIPT_DIR / ""
OUTPUT_DIR.mkdir(exist_ok=True)

if not LCSC_FILE.exists():
    print(f"Error: {LCSC_FILE} not found")
    sys.exit(1)

# Read part numbers
with open(LCSC_FILE, "r", encoding="utf-8") as f:
    part_numbers = [
        line.strip()
        for line in f
        if line.strip() and not line.strip().startswith("#")
    ]

print(f"Found {len(part_numbers)} part numbers")

for part in part_numbers:
    print(f"Downloading {part}...")

    cmd = [
        "easyeda2kicad",
        "--full",
        f"--lcsc_id={part}",
        "--output",
        str(OUTPUT_DIR)
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"✓ {part}")
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed: {part} ({e})")

print("Done.")