import os
from PIL import Image
import OpenImageIO as oiio

def convert_exr_to_jpg(input_dir, output_dir, compression=90):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all the files in the input directory
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.exr'):
            input_file_path = os.path.join(input_dir, file_name)
            output_file_path = os.path.join(output_dir, file_name.replace('.exr', '.jpg'))

            try:
                # Open the EXR file using OpenImageIO
                exr_image = oiio.ImageInput.open(input_file_path)
                spec = exr_image.spec()
                data = exr_image.read_image(format='float')
                exr_image.close()

                # Create a Pillow image object from the EXR data
                image = Image.fromarray((data * 255).astype('uint8'))

                # Save as JPG with specified compression
                image.save(output_file_path, 'JPEG', quality=compression)
                print(f"Converted: {file_name} to {output_file_path}")
            except Exception as e:
                print(f"Failed to convert {file_name}: {e}")

if __name__ == "__main__":
    input_directory = '/mnt/8TBdrive/bald_guy/Camera_inputs/'
    output_directory = '/mnt/8TBdrive/bald_guy/Camera_inputs_jpg/'
    convert_exr_to_jpg(input_directory, output_directory)
