import sys
import os
import argparse

parser = argparse.ArgumentParser(
    description="Count lines, words, and bytes in files."
)

parser.add_argument("-l", action="store_true", help="Count lines")
parser.add_argument("-w", action="store_true", help="Count words")
parser.add_argument("-c", action="store_true", help="Count bytes")
parser.add_argument("filenames", nargs="+")

args = parser.parse_args()

count_lines = args.l
count_words = args.w
count_bytes = args.c
filenames = args.filenames

def format_counts(line_count, word_count, byte_count):
    output = []

    if count_lines:
        output.append(line_count)

    if count_words:
        output.append(word_count)

    if count_bytes:
        output.append(byte_count)

    if not count_lines and not count_words and not count_bytes:
        output.append(line_count)
        output.append(word_count)
        output.append(byte_count)

    formatted_output = []

    for number in output:
        formatted_output.append(f"{number:3}")

    return " ".join(formatted_output)

total_lines = 0
total_words = 0
total_bytes = 0

for filename in filenames:
    file = open(filename)

    line_count = 0
    word_count = 0

    for line in file:
        line_count += 1
        word_count += len(line.split())

    byte_count = os.path.getsize(filename)

    total_lines += line_count
    total_words += word_count
    total_bytes += byte_count

    print(
        format_counts(line_count, word_count, byte_count),
        filename,
    )

if len(filenames) > 1:
    print(
        format_counts(total_lines, total_words, total_bytes),
        "total",
    )
