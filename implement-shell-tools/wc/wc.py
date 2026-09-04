import sys
import os

count_lines = "-l" in sys.argv
count_words = "-w" in sys.argv
count_bytes = "-c" in sys.argv

filenames = []

for argument in sys.argv[1:]:
    if not argument.startswith("-"):
        filenames.append(argument)

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
