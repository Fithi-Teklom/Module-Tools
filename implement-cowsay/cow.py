import cowsay
import argparse

parser = argparse.ArgumentParser(
    prog="cowsay",
    description="Make animals say things",
)

parser.add_argument(
    "message",
    nargs="+",
    help="The message to say.",
)

parser.add_argument(
    "--animal",
    choices = cowsay.char_names,
    default="cow",
    help="The animal to be saying things.",
)

args = parser.parse_args()
message = " ".join(args.message)

animal_function = getattr(cowsay, args.animal)

animal_function(message)

# print(message)
# print(args.animal)