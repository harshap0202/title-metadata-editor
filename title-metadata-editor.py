#Author : Harshwardhan Patil
import os
import subprocess

def set_title_as_filename(file_path, output_folder):
    # Get the file name without extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # Use ffmpeg to set the title metadata
    output_path = os.path.join(output_folder, f'{file_name}.mkv')
    command = [
        r"C:/ffmpeg/ffmpeg.exe",  # Replace with the actual path to ffmpeg
        '-i', file_path,
        '-c', 'copy',
        '-metadata', f'title={file_name}',
        output_path
    ]

    try:
        # Redirect stdout and stderr to suppress detailed ffmpeg output
        with open(os.devnull, 'w') as null:
            subprocess.run(command, check=True, stdout=null, stderr=null)

        print(f"Title metadata for '{file_path}' set successfully. Output saved to '{output_path}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Specify the folder path where MKV files are located
    folder_path = 'Folder Name'
    # Create 'edited' folder within the specified folder path
    output_folder = os.path.join(folder_path, 'edited')
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all MKV files in the specified folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".mkv"):
            file_path = os.path.join(folder_path, filename)
            set_title_as_filename(file_path, output_folder)
