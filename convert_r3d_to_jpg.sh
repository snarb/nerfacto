#!/bin/bash

# Directory containing R3D files
input_dir="/home/brans/Downloads/video/TheEgg_subclip_01"

# Change to the input directory
cd "$input_dir" || { echo "Failed to change directory to $input_dir"; exit 1; }

# Loop through each R3D file in the directory
for r3d_file in "$input_dir"/*.R3D; do
    # Check if any R3D files exist
    if [[ ! -e $r3d_file ]]; then
        echo "No R3D files found in $input_dir"
        exit 1
    fi
    
    # Extract the base name of the file (without extension)
    base_name=$(basename "$r3d_file" .R3D)

    # Create output directory based on the base name
    output_dir="$input_dir/$base_name/frames"
    mkdir -p "$output_dir"

    # Run REDline command to convert R3D to JPG frames
    REDline -i "$r3d_file" --format 3 -o "$output_dir"

    echo "Converted $r3d_file to JPEG frames in $output_dir"
done

