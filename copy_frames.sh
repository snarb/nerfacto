#!/bin/bash

# Source and target directories
SOURCE_DIR="/home/brans/Downloads/video/TheEgg_subclip_01"
TARGET_DIR="/home/brans/Downloads/video/result"

# Ensure the target directory exists
mkdir -p "$TARGET_DIR"

# Loop through each subfolder in the source directory
for SUBFOLDER in "$SOURCE_DIR"/*; do
  if [ -d "$SUBFOLDER" ]; then
    # Get the name of the subfolder
    SUBFOLDER_NAME=$(basename "$SUBFOLDER")
    
    # Define the source file path and the target file path
    SOURCE_FILE="$SUBFOLDER/frames.000001.jpg"
    TARGET_FILE="$TARGET_DIR/$SUBFOLDER_NAME.jpg"
    
    # Copy the file if it exists
    if [ -f "$SOURCE_FILE" ]; then
      cp "$SOURCE_FILE" "$TARGET_FILE"
      echo "Copied $SOURCE_FILE to $TARGET_FILE"
    else
      echo "File $SOURCE_FILE does not exist"
    fi
  fi
done

