import sys
import os

show_all = "-a" in sys.argv
one_per_line = "-1" in sys.argv

paths = []

for argument in sys.argv[1:]:
    if not argument.startswith("-"):
        paths.append(argument)

if not paths:
    paths.append(".")

for path in paths:
    if os.path.isfile(path):
        if len(paths) == 1 or one_per_line:
            print(path)
        else:
            print(path, end = ("  "))
    else:
        if len(paths) > 1:
            print()
            print()
            print(path + ":")

        files = sorted(os.listdir(path))

        if show_all:
            files = ["."] + [".."] + files

        for file in files:
            if show_all or not file.startswith("."):
                if one_per_line:
                    print(file)
                else:
                    print(file, end=("  ")) 
        if not one_per_line:
            print()


