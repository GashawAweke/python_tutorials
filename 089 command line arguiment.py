# Python provides:

# import sys
# Command-line Arguments

# Arguments are stored in:
# sys.argv


# Example


import argparse
import sys

print(sys.argv)


# Access Arguments

name = sys.argv[1]

print(name)


# Better Approach: argparse
# Modern Python uses:

parser = argparse.ArgumentParser()

parser.add_argument("--name")
parser.add_argument("--age", type=int)

args = parser.parse_args()

print(args.name)
print(args.age)


# Production Example

# Backup utility:

python3 backup.py - -source data - -dest backups

# Machine learning:

python3 train.py - -epochs 100 - -lr 0.001

# Server:

python3 server.py - -port 8000

# Most professional Python tools use argparse.
