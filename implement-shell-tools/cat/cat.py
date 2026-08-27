import sys

if sys.argv[1] == "-n" or sys.argv[1] == "-b":
   filenames = sys.argv[2:]
else:
   filenames = sys.argv[1:]
line_number = 1
for filename in filenames:
    file = open(filename)
    for line in file:
        if sys.argv[1] == "-n":
           print(line_number, line, end = "")
           line_number += 1
        elif sys.argv[1]== "-b":
            if line.strip() != "":
                print(line_number, line, end = "")
                line_number += 1
            else:
                print(line, end="")    
        else:
           print(line, end = "")    
