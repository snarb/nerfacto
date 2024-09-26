import os
import subprocess

INPUT_DATASET_DIR = '/mnt/new_drive/glasses/Camera_inputs/'
OUTPUT_DATASET_DIR = '/mnt/new_drive/glasses/Camera_inputs/preprocessed'
PROCESS_SCRIPT = '/home/ainaadmin/pavlo/nerfacto/nerfstudio/scripts/process_data.py'

# Create the output directory if it doesn't exist
if not os.path.exists(OUTPUT_DATASET_DIR):
    os.makedirs(OUTPUT_DATASET_DIR)

# List all subdirectories in the input dataset directory
subdirs = [d for d in os.listdir(INPUT_DATASET_DIR) if os.path.isdir(os.path.join(INPUT_DATASET_DIR, d))]
total_subdirs = len(subdirs)

for idx, subdir in enumerate(sorted(subdirs)):
    input_training_dir = os.path.join(INPUT_DATASET_DIR, subdir)
    output_dir = os.path.join(OUTPUT_DATASET_DIR, subdir)

    # Create output directory for the current frame if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Build the command to execute
    command = [
        'python3', PROCESS_SCRIPT,
        'images',
        '--data', input_training_dir,
        #'--eval_data', input_evaluation_dir,
        '--output-dir', output_dir,
        '--skip_colmap'
    ]

    # Print the command for debugging purposes
    print(f"Running command: {' '.join(command)}")

    # Execute the command
    subprocess.run(command, check=True)

    # Print progress
    print(f"Processed folder {idx + 1} of {total_subdirs}")
