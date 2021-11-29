# Image Converter and Metadata / EXIF Stripper
This is a simple image converter and metadata / EXIF stripper for use in Unix/Linux command line.

Drop images into the "input" folder and hit "sh start_and_run.sh" and it will convert them to JPG, strip the metadata and move them to the "output" folder in a time-stamped sub-folder.  (It will also copy the originals to the "originals" folder, and will remove them from the input folder.)

## Prerequisites
Unix/Linux Terminal
Python 3.x

## Setup
git clone https://github.com/pysogge/image_converter_exif_remover.git
cd ./image_converter_exif_remover
sh setup_venv.sh

## Usage (once setup is complete - see above)
1. Manually place your files into the input folder (do not use subfolders)
2. sh start_and_run.sh
3. Watch the progress bar
4. Collect your files in the timestamped output folder
5. done.

### Credits
Progress bar function from: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

### Notes
This script runs the image processing synchronously

The original reason for creating this script was to upload images to marketplace sites without exposing all of the rich metadata and location information.  This is a simple step to protect privacy.