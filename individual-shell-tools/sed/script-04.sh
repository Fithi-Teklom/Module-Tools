#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt replacing every occurrence of the string "We'll" with "We will".
# The output should contain 11 lines.

sed "s/We'll/We will/g" individual-shell-tools/sed/input.txt