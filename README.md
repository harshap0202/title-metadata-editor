# Title Metadata Setter for MKV Files

This Python script sets the title metadata of MKV files to their respective filenames using FFmpeg.

## Usage

1. **Prerequisites**: 
   - Python
   - FFmpeg installed on your system. You can download it from [here](https://ffmpeg.org/download.html).

2. **Installation**:
   - Clone this repository to your local machine:

     ```bash
     https://github.com/harshap0202/title-metadata-editor.git
     ```
     
3. **Input**:
   - Place the MKV files you want to modify in the specified folder.

4. **Output**:
   - The script will create an "edited" folder within the specified folder and overwrite the original MKV files with the modified ones.

5. **Usage**:
   - Locate ffmpeg.exe and place that on line 12 of the code
   - Select a folder with all the mkv files
   - PLace the folder path in the code as such : <br>
     Folder path : "E:\Modern Family\Season 01" --(turns)--> "E:\\Modern Family\\Season 01"
     
   - Run the script with the following command:
     ```bash
     python title_metadata.py
     ```

## Troubleshooting

- If you encounter any issues or errors during script execution, ensure that FFmpeg is installed correctly and that the specified folder path is correct.
