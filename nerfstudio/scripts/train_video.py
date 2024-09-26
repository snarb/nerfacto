import os
import subprocess

INPUT_DATASET_DIR = '/mnt/new_drive/glasses/Camera_inputs/preprocessed' #'/home/brans/Downloads/video/output/'
OUTPUT_DATASET_DIR = '/home/ainaadmin/pavlo/checkpoints'
PROCESS_SCRIPT = '/home/ainaadmin/pavlo/nerfacto/nerfstudio/scripts/train.py'
MAX_NUM_ITERATIONS = 15000
VIS_MODE = 'wandb'
PROJECT_NAME = 'video'
EVAL_MODE = 'fraction' #'filename'
LOAD_DIR = '/home/ainaadmin/pavlo/nerfacto/scripts/outputs/000202/splatfacto/2024-08-05_192900/nerfstudio_models'

# Create the output directory if it doesn't exist
if not os.path.exists(OUTPUT_DATASET_DIR):
    os.makedirs(OUTPUT_DATASET_DIR)

# List all subdirectories in the input dataset directory
subdirs = [d for d in os.listdir(INPUT_DATASET_DIR) if os.path.isdir(os.path.join(INPUT_DATASET_DIR, d))]
total_subdirs = len(subdirs)

for idx, subdir in enumerate(sorted(subdirs)):
    print(f'Processing: {subdir}. {idx} from {len(subdirs)}')
    input_training_dir = os.path.join(INPUT_DATASET_DIR, subdir)
    output_dir = os.path.join(OUTPUT_DATASET_DIR, f"frame_{idx}")

    # Create output directory for the current frame if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Build the command to execute
    command = [
        'python3', PROCESS_SCRIPT,
        'splatfacto',
        #'splatfacto-big',
        '--output_dir', output_dir,
        #'--load-dir', LOAD_DIR,
        '--max-num-iterations', str(MAX_NUM_ITERATIONS),
        '--data', input_training_dir,
        '--vis', VIS_MODE,
        '--project_name', PROJECT_NAME,
        '--load_scheduler', 'False',
        'nerfstudio-data',
        #'--eval-mode', EVAL_MODE,
    ]

    # Print the command for debugging purposes
    print(f"Running command: {' '.join(command)}")

    # Execute the command
    subprocess.run(command, check=True)

    # Print progress
    print(f"Processed folder {idx + 1} of {total_subdirs}")
