#!/bin/bash

# Source and target directories
SOURCE_DIR="/home/brans/Downloads/video/TheEgg_subclip_01"
DATASET_DIR="/home/brans/Downloads/video/dataset"

# Loop through each subfolder in the source directory
for SUBFOLDER in "$SOURCE_DIR"/*; do
  if [ -d "$SUBFOLDER" ]; then
    # Get the name of the subfolder
    SUBFOLDER_NAME=$(basename "$SUBFOLDER")
    
    # Loop through the frames and copy them to their respective subfolders
    for FRAME_NUM in $(seq -f "%06g" 0 209); do
      SOURCE_FILE="$SUBFOLDER/frames.$FRAME_NUM.jpg"
      
      # Determine the target directory based on the subfolder name
      if [ "$SUBFOLDER_NAME" == "C001_C094_062611_001" ] || [ "$SUBFOLDER_NAME" == "G001_D094_0626PB_001" ]; then
        TARGET_SUBDIR="evaluation"
      else
        TARGET_SUBDIR="training"
      fi
      
      # Define the frame subfolder and the target file path
      FRAME_SUBFOLDER="$DATASET_DIR/$FRAME_NUM/$TARGET_SUBDIR"
      FRAME_TARGET="$FRAME_SUBFOLDER/$SUBFOLDER_NAME.jpg"
      
      # Ensure the subfolder in the target directory exists
      mkdir -p "$FRAME_SUBFOLDER"
      
      # Copy the file if it exists
      if [ -f "$SOURCE_FILE" ]; then
        cp "$SOURCE_FILE" "$FRAME_TARGET"
        echo "Copied $SOURCE_FILE to $FRAME_TARGET"
      else
        echo "File $SOURCE_FILE does not exist"
      fi
    done
  fi
done

