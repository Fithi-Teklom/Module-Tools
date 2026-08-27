import sys
import os

count_lines = "-l" in sys.argv
count_words = "-w" in sys.argv
count_bytes = "-c" in sys.argv
filenames = []

for argument in sys.argv[1:]:
    if not argument.startswith("-"):
        filenames.append(argument)

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

    print(" ".join(formatted_output), filename)

if len(filenames) > 1:
    total_output = []

    if count_lines:
        total_output.append(total_lines)

    if count_words:
        total_output.append(total_words)

    if count_bytes:
        total_output.append(total_bytes)

    if not count_lines and not count_words and not count_bytes:
        total_output.append(total_lines)
        total_output.append(total_words)
        total_output.append(total_bytes)
        
    formatted_total = []

    for number in total_output:
        formatted_total.append(f"{number:3}")
    print(" ".join(formatted_total), "total")
