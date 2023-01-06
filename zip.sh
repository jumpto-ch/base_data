#!/bin/bash

# Iterate through each subdirectory in the current directory
for dir in */; do
    # Create a zip file with the same name as the directory
    zip -r "${dir%/}.zip" "$dir"
done
