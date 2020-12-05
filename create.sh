#!/usr/bin/env bash

set -e

DAY=$1
FOLDER="day${DAY}"

echo "Creating day ${DAY}"

mkdir "${FOLDER}"

echo "from .solve import solve" > "${FOLDER}/__init__.py"
cat <<EOF > "${FOLDER}/solve.py"
def solve(input):
    pass
EOF

touch "${FOLDER}/input.txt"
echo "[Advent of Code - Day ${DAY}](https://adventofcode.com/2020/day/${DAY})" \
    > "${FOLDER}/README.md"
